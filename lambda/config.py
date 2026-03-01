"""
Search keywords, countries, and scoring configuration.
"""

COUNTRIES = ["Netherlands", "Colombia", "Australia"]

DEVOPS_CLOUD_KEYWORDS = [
    "Solutions Architect",
    "Cloud Architect",
    "DevOps Engineer",
    "Site Reliability Engineer",
    "Platform Engineer",
    "Infrastructure Architect",
    "AWS Architect",
    "Azure Architect",
    "Cloud Engineer",
]

DATA_AI_KEYWORDS = [
    "Data Engineer",
    "AI Engineer",
    "ML Engineer",
    "Data Architect",
    "MLOps Engineer",
    "AI Solutions Architect",
    "Data Platform Engineer",
    "GenAI Engineer",
]

SEARCH_PROFILES = {
    "DevOps/Cloud": DEVOPS_CLOUD_KEYWORDS,
    "Data/AI": DATA_AI_KEYWORDS,
}

# Words that boost relevance when found in job title
CLOUD_KEYWORDS = {"aws", "azure", "gcp", "google cloud", "multi-cloud", "cloud"}
DEVOPS_KEYWORDS = {"terraform", "kubernetes", "docker", "ci/cd", "devops", "sre", "infrastructure", "serverless", "iac", "k8s"}
SENIORITY_KEYWORDS = {"senior", "lead", "principal", "staff", "head"}
DATA_AI_KEYWORDS_SCORE = {"machine learning", "ai", "data", "ml", "llm", "genai", "nlp", "analytics", "deep learning"}

# Max pages to scrape per keyword+location (25 results per page)
MAX_PAGES = 4

# Delay between requests in seconds
REQUEST_DELAY = 1.5
