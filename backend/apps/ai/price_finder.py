import random
import logging

# Configure logging for this module
logger = logging.getLogger(__name__)

def fetch_prices_from_stores(search_query):
    """
    Simulate fetching price information from online stores based on a search query.
    Replace this later with real API calls to Amazon, Walmart, Best Buy, etc.
    """
    logger.debug(f"🛒 Fetching prices for: {search_query}")

    simulated_prices = {
        "Amazon": round(random.uniform(50, 200), 2),
        "Walmart": round(random.uniform(50, 200), 2),
        "Best Buy": round(random.uniform(50, 200), 2),
        "Home Depot": round(random.uniform(50, 200), 2),
        "Target": round(random.uniform(50, 200), 2),
    }

    # Generate fake URLs based on store name and search_query
    results = []
    for store, price in simulated_prices.items():
        query_for_url = search_query.lower().replace(" ", "+")
        fake_url = f"https://{store.replace(' ', '').lower()}.com/search?q={query_for_url}"
        results.append({
            "store": store,
            "price": price,
            "url": fake_url
        })

    logger.debug(f"🛒 Price results: {results}")
    return results
