"""Minimal example: run the leboncoin-cars-scraper Actor and print the results.

Usage: APIFY_TOKEN=... python run.py   (pip install apify-client)
"""
import os
import sys

from apify_client import ApifyClient

token = os.environ.get("APIFY_TOKEN")
if not token:
    sys.exit("Set the APIFY_TOKEN environment variable first.")

client = ApifyClient(token)

run_input = {
    "query": "break diesel",
    "brand": "PEUGEOT",
    "maxMileageKm": 150000,
    "maxItems": 50,
}

run = client.actor("bibian/leboncoin-cars-scraper").call(run_input=run_input)

count = 0
for item in client.dataset(run.default_dataset_id).iterate_items():
    count += 1
    print(f"{item['title']} | {item.get('price')} EUR | {item.get('mileageKm')} km | {item.get('dealerName')}")
print(f"{count} results")
