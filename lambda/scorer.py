"""
Relevance scoring engine.
Scores each job 0-100 based on keyword matching against Jefferson's profiles.
"""

from config import (
    CLOUD_KEYWORDS,
    DATA_AI_KEYWORDS_SCORE,
    DEVOPS_KEYWORDS,
    SENIORITY_KEYWORDS,
)


def score_job(job: dict, profile: str) -> int:
    """
    Score a job 0-100.

    profile: "DevOps/Cloud" or "Data/AI" -- shifts weights accordingly.
    """
    title_lower = job.get("title", "").lower()

    cloud_score = _keyword_score(title_lower, CLOUD_KEYWORDS)
    devops_score = _keyword_score(title_lower, DEVOPS_KEYWORDS)
    seniority_score = _seniority_score(title_lower)
    data_ai_score = _keyword_score(title_lower, DATA_AI_KEYWORDS_SCORE)
    title_score = _title_relevance(title_lower, profile)

    if profile == "DevOps/Cloud":
        total = (
            title_score * 0.35
            + cloud_score * 0.25
            + devops_score * 0.20
            + seniority_score * 0.10
            + data_ai_score * 0.10
        )
    else:  # Data/AI
        total = (
            title_score * 0.35
            + data_ai_score * 0.25
            + cloud_score * 0.10
            + devops_score * 0.10
            + seniority_score * 0.10
            + _keyword_score(title_lower, {"data", "ml", "ai", "genai", "llm", "analytics"}) * 0.10
        )

    return min(100, max(0, round(total)))


def _keyword_score(text: str, keywords: set) -> int:
    """Score 0-100 based on how many keywords appear in text."""
    if not text:
        return 0
    matches = sum(1 for kw in keywords if kw in text)
    if matches == 0:
        return 0
    return min(100, matches * 40)


def _seniority_score(title: str) -> int:
    """Score based on seniority level in title."""
    for word in SENIORITY_KEYWORDS:
        if word in title:
            return 100
    if "junior" in title or "intern" in title or "entry" in title:
        return 0
    return 40  # mid-level default


def _title_relevance(title: str, profile: str) -> int:
    """Score how well title matches the target profile roles."""
    if profile == "DevOps/Cloud":
        high_match = [
            "solutions architect", "cloud architect", "devops",
            "platform engineer", "infrastructure", "sre",
            "site reliability", "aws architect", "azure architect",
            "cloud engineer",
        ]
    else:
        high_match = [
            "data engineer", "ai engineer", "ml engineer",
            "data architect", "mlops", "ai solutions",
            "data platform", "genai", "machine learning",
            "data scientist",
        ]

    for role in high_match:
        if role in title:
            return 100

    # Partial matches
    partial_keywords = {"architect", "engineer", "cloud", "devops", "data", "ai", "ml"}
    matches = sum(1 for kw in partial_keywords if kw in title)
    return min(80, matches * 25)
