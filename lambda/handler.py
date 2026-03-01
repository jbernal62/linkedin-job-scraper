"""
Lambda entry point.
Called by EventBridge schedule or manual invocation.
"""

from config import COUNTRIES, SEARCH_PROFILES
from scorer import score_job
from scraper import search_linkedin_jobs
from sheets import write_jobs_to_sheet


def lambda_handler(event, context):
    """
    Main entry point.

    event can optionally contain:
      - "countries": ["Netherlands"]  -- override which countries to scan
      - "profiles": ["DevOps/Cloud"]  -- override which profiles to search
    """
    countries = event.get("countries", COUNTRIES)
    profiles = event.get("profiles", SEARCH_PROFILES)
    if isinstance(profiles, list):
        profiles = {p: SEARCH_PROFILES[p] for p in profiles if p in SEARCH_PROFILES}

    all_results = {}

    for country in countries:
        print(f"Scanning {country}...")
        country_jobs = []
        seen_links = set()

        for profile_name, keywords_list in profiles.items():
            for keywords in keywords_list:
                print(f"  Searching: {keywords} in {country} ({profile_name})")
                jobs = search_linkedin_jobs(keywords, country)
                print(f"    Found {len(jobs)} results")

                for job in jobs:
                    if job["link"] not in seen_links:
                        seen_links.add(job["link"])
                        job["score"] = score_job(job, profile_name)
                        job["profile"] = profile_name
                        country_jobs.append(job)

        # Sort by score descending
        country_jobs.sort(key=lambda j: j["score"], reverse=True)
        all_results[country] = country_jobs

        # Write to Google Sheets
        write_jobs_to_sheet(country, country_jobs)

    total = sum(len(v) for v in all_results.values())
    summary = {c: len(v) for c, v in all_results.items()}
    msg = f"Scraped {total} unique jobs: {summary}"
    print(msg)

    return {
        "statusCode": 200,
        "body": msg,
        "details": summary,
    }
