import cloudscraper
import statistics
import json
import re
import urllib.parse
import time

# Create a UK-based scraper session
scraper = cloudscraper.create_scraper(
    browser={"browser": "chrome", "platform": "windows", "mobile": False},
    headers={"x-vinted-frontend-id": "23"}
)

def vinted_price_stats(q: str, n: int = 50):
    base_api = (
        "https://www.vinted.co.uk/api/v2/catalog/items?"
        f"search_text={urllib.parse.quote_plus(q)}&per_page={n}"
    )

    # Try both page 1 and page 2 to bypass lazy loading
    for page in (1, 2):
        try:
res = scraper.get(f"{base_api}&page={page}", timeout=10)
