"""
Scrapes LinkedIn's public guest job search API.
No authentication required.
"""

import time
from typing import Optional

import requests
from bs4 import BeautifulSoup

from config import MAX_PAGES, REQUEST_DELAY

BASE_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml",
}


def search_linkedin_jobs(
    keywords: str,
    location: str,
    max_pages: int = MAX_PAGES,
) -> list[dict]:
    """
    Search LinkedIn public job listings.

    Returns list of dicts: {title, company, location, link, date_posted}
    """
    all_jobs = []

    for page in range(max_pages):
        start = page * 25
        params = {
            "keywords": keywords,
            "location": location,
            "f_WT": "2",        # Remote only
            "sortBy": "DD",     # Most recent
            "start": str(start),
        }

        try:
            resp = requests.get(
                BASE_URL, params=params, headers=HEADERS, timeout=15
            )
            if resp.status_code != 200:
                print(f"  HTTP {resp.status_code} for {keywords} in {location} page {page}")
                break

            jobs = _parse_job_cards(resp.text)
            if not jobs:
                break

            all_jobs.extend(jobs)
            time.sleep(REQUEST_DELAY)

        except requests.RequestException as e:
            print(f"  Request error for {keywords} in {location}: {e}")
            break

    return all_jobs


def _parse_job_cards(html: str) -> list[dict]:
    """Parse job card HTML from LinkedIn guest API response."""
    soup = BeautifulSoup(html, "html.parser")
    jobs = []

    cards = soup.find_all("div", class_="base-card")
    if not cards:
        cards = soup.find_all("li")

    for card in cards:
        job = _extract_job_from_card(card)
        if job and job.get("title") and job.get("link"):
            jobs.append(job)

    return jobs


def _extract_job_from_card(card) -> Optional[dict]:
    """Extract job info from a single card element."""
    try:
        title_el = card.find("h3", class_="base-search-card__title")
        company_el = card.find("h4", class_="base-search-card__subtitle")
        location_el = card.find("span", class_="job-search-card__location")
        link_el = card.find("a", class_="base-card__full-link")
        date_el = card.find("time")

        if not title_el:
            return None

        title = title_el.get_text(strip=True) if title_el else ""
        company = company_el.get_text(strip=True) if company_el else ""
        location = location_el.get_text(strip=True) if location_el else ""
        link = link_el["href"].split("?")[0] if link_el and link_el.get("href") else ""
        date_posted = date_el.get("datetime", "") if date_el else ""

        if not title or not link:
            return None

        return {
            "title": title,
            "company": company,
            "location": location,
            "link": link,
            "date_posted": date_posted,
        }
    except Exception:
        return None
