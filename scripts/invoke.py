"""
Invoke the job scraper Lambda on-demand.

Usage:
    python scripts/invoke.py
    python scripts/invoke.py --country Netherlands
    python scripts/invoke.py --country Netherlands --country Colombia
"""

import argparse
import json

import boto3


def invoke(countries=None):
    client = boto3.client("lambda", region_name="us-east-1")
    payload = {}
    if countries:
        payload["countries"] = countries

    print(f"Invoking job-scraper-processor with payload: {json.dumps(payload)}")

    response = client.invoke(
        FunctionName="job-scraper-processor",
        InvocationType="RequestResponse",
        Payload=json.dumps(payload),
    )

    result = json.loads(response["Payload"].read())
    print(json.dumps(result, indent=2))
    return result


def main():
    parser = argparse.ArgumentParser(description="Invoke LinkedIn job scraper Lambda")
    parser.add_argument(
        "--country",
        action="append",
        help="Country to scan (can be repeated). Defaults to all 3.",
    )
    args = parser.parse_args()
    invoke(args.country)


if __name__ == "__main__":
    main()
