import requests
import statistics
import urllib.parse

def vinted_price_stats(search):
    base_api = (
        "https://www.vinted.co.uk/api/v2/catalog/items?"
        f"search_text={urllib.parse.quote_plus(search)}&per_page=20"
    )

    prices = []
    total_results = 0

    # Try to gather prices from the first few pages
    for page in range(1, 4):
        try:
            res = requests.get(f"{base_api}&page={page}", timeout=10)
            res.raise_for_status()
            items = res.json().get("items", [])

            for item in items:
                price = item.get("price", {}).get("amount")
                if price:
                    prices.append(float(price))

            total_results += len(items)
        except Exception as e:
            print(f"Failed on page {page}:", e)
            continue

    if not prices:
        return {"low": 0, "median": 0, "high": 0, "count": 0}

    return {
        "low": min(prices),
        "median": round(statistics.median(prices), 2),
        "high": max(prices),
        "count": total_results,
  }
