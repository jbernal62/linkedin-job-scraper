"""
Writes job scraping results to Google Sheets.
Adapted from invoice-tracker/lambda/sheets.py pattern.
"""

import json
import os
from datetime import datetime, timezone

import boto3
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SHEET_NAME = os.environ.get("GOOGLE_SHEET_NAME", "LinkedIn Job Scraper")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

HEADERS = [
    "Scan Date",
    "Position Title",
    "Company",
    "Relevance Score",
    "Profile Match",
    "Country",
    "Link to Apply",
]

COL = {h: i for i, h in enumerate(HEADERS)}

_secrets_client = boto3.client("secretsmanager", region_name="us-east-1")
_creds = None


def _get_creds():
    global _creds
    if _creds is None:
        resp = _secrets_client.get_secret_value(
            SecretId=os.environ["GOOGLE_SECRET_NAME"]
        )
        sa_info = json.loads(resp["SecretString"])
        _creds = Credentials.from_service_account_info(sa_info, scopes=SCOPES)
    return _creds


def _get_or_create_worksheet(spreadsheet, tab_name: str) -> gspread.Worksheet:
    try:
        return spreadsheet.worksheet(tab_name)
    except gspread.exceptions.WorksheetNotFound:
        ws = spreadsheet.add_worksheet(
            title=tab_name, rows=1000, cols=len(HEADERS)
        )
        return ws


def _ensure_headers(ws: gspread.Worksheet):
    first_row = ws.row_values(1)
    if not first_row or first_row[0] != HEADERS[0]:
        ws.update("A1", [HEADERS])
        _apply_formatting(ws)


def _apply_formatting(ws: gspread.Worksheet):
    """Apply header styling, frozen row, filter, relevance colors."""
    service = build("sheets", "v4", credentials=_get_creds())
    ss_id = ws.spreadsheet.id
    sheet_id = ws.id
    num_cols = len(HEADERS)

    requests_list = [
        # Freeze row 1
        {
            "updateSheetProperties": {
                "properties": {
                    "sheetId": sheet_id,
                    "gridProperties": {"frozenRowCount": 1},
                },
                "fields": "gridProperties.frozenRowCount",
            }
        },
        # Dark blue header row
        {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 0, "endRowIndex": 1,
                    "startColumnIndex": 0, "endColumnIndex": num_cols,
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 0.118, "green": 0.220, "blue": 0.392},
                        "textFormat": {
                            "bold": True,
                            "foregroundColor": {"red": 1, "green": 1, "blue": 1},
                        },
                        "horizontalAlignment": "CENTER",
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)",
            }
        },
        # Enable filter
        {
            "setBasicFilter": {
                "filter": {
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": 0, "endRowIndex": 1,
                        "startColumnIndex": 0, "endColumnIndex": num_cols,
                    }
                }
            }
        },
    ]

    # Relevance Score conditional formatting
    for text, color in [
        (">=70", {"red": 0.18, "green": 0.66, "blue": 0.33}),   # Green
        (">=40", {"red": 1.0,  "green": 0.60, "blue": 0.0}),    # Orange
    ]:
        value = text.replace(">=", "")
        requests_list.append({
            "addConditionalFormatRule": {
                "rule": {
                    "ranges": [{
                        "sheetId": sheet_id,
                        "startRowIndex": 1, "endRowIndex": 1000,
                        "startColumnIndex": COL["Relevance Score"],
                        "endColumnIndex": COL["Relevance Score"] + 1,
                    }],
                    "booleanRule": {
                        "condition": {
                            "type": "NUMBER_GREATER_THAN_EQ",
                            "values": [{"userEnteredValue": value}],
                        },
                        "format": {
                            "backgroundColor": color,
                            "textFormat": {
                                "bold": True,
                                "foregroundColor": {"red": 1, "green": 1, "blue": 1},
                            },
                        },
                    },
                },
                "index": 0,
            }
        })

    service.spreadsheets().batchUpdate(
        spreadsheetId=ss_id, body={"requests": requests_list}
    ).execute()


def write_jobs_to_sheet(country: str, jobs: list[dict]):
    """Write jobs for a country to its own tab in the spreadsheet."""
    gc = gspread.authorize(_get_creds())
    spreadsheet = gc.open(SHEET_NAME)
    ws = _get_or_create_worksheet(spreadsheet, country)
    _ensure_headers(ws)

    # Clear existing data rows (keep header)
    row_count = len(ws.get_all_values())
    if row_count > 1:
        ws.delete_rows(2, row_count)

    if not jobs:
        print(f"  No jobs found for {country}")
        return

    scan_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    rows = []
    for job in jobs:
        link = job.get("link", "")
        link_formula = f'=HYPERLINK("{link}","Apply")' if link else ""
        rows.append([
            scan_date,
            job.get("title", ""),
            job.get("company", ""),
            job.get("score", 0),
            job.get("profile", ""),
            country,
            link_formula,
        ])

    ws.append_rows(rows, value_input_option="USER_ENTERED")

    # Sort by relevance score descending
    service = build("sheets", "v4", credentials=_get_creds())
    service.spreadsheets().batchUpdate(
        spreadsheetId=ws.spreadsheet.id,
        body={
            "requests": [{
                "sortRange": {
                    "range": {
                        "sheetId": ws.id,
                        "startRowIndex": 1, "endRowIndex": 1000,
                        "startColumnIndex": 0, "endColumnIndex": len(HEADERS),
                    },
                    "sortSpecs": [{
                        "dimensionIndex": COL["Relevance Score"],
                        "sortOrder": "DESCENDING",
                    }],
                }
            }]
        },
    ).execute()

    print(f"  Wrote {len(rows)} jobs to {country} tab")
