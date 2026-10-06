# How to Scrape Leboncoin Car Listings (Dealers Only, Price, Mileage, Year)

> **Run it now, no code: [leboncoin-cars-scraper on the Apify Store](https://apify.com/bibian/leboncoin-cars-scraper)** &nbsp;|&nbsp; $5.00 per 1,000 listings &nbsp;|&nbsp; residential proxy, no login

Leboncoin is France's largest classifieds site, including a huge used-car market. It has no public export and no official API for third parties, and its anti-bot defenses (DataDome) block plain requests and datacenter proxies outright. This guide shows how to get professional car listings as clean structured data: brand, model, year, mileage, price, fuel, gearbox, color, dealer name and location.

Searches this page answers: leboncoin scraper, leboncoin voitures scraper, french car classifieds scraper, leboncoin api.

## What you get from the Leboncoin cars scraper

- Every professional car listing matching your filters, newest first, with brand, model, year and mileage.
- Price in EUR, fuel type, gearbox and color.
- Dealer name and French business registration number (SIREN), never a private seller.
- Location (city, postal code, department, region) and listing photos.

Export the dataset as JSON, CSV or Excel, or read it through the Apify API. A real sample (five results) is in [`sample-output.json`](sample-output.json).

## Output fields

| Field | What it is |
|---|---|
| `id`, `url` | Leboncoin listing id and public link |
| `title` | Listing title as published |
| `price` | Price in EUR |
| `brand`, `model`, `year` | Vehicle brand, model and registration year |
| `mileageKm`, `fuel`, `gearbox`, `color` | Specifications |
| `city`, `zipcode`, `department`, `region` | Location |
| `dealerName`, `dealerSiren` | Dealership's public trade name and French business registration number |
| `firstPublicationDate` | When the listing first went online |
| `imageUrl`, `imageCount` | Thumbnail and number of photos |

## Use cases

- **Monitor dealer stock.** Track what a market segment of professional sellers is listing, by brand, price or mileage.
- **Feed a car-buying alert.** Run it daily with your filters and get only new listings.
- **Benchmark prices.** Compare price, mileage and year across dealers for the same model.
- **Build a car marketplace aggregator.** Leboncoin has no public export for third parties; this Actor reads the same listings its own search page shows.

## Input

| Field | What it does |
|---|---|
| `query` | Free text search, exactly as typed in Leboncoin's own search box, for example `break diesel`. Empty means every professional listing. |
| `brand` | Car brand, for example `PEUGEOT`. Empty for all brands. |
| `minPrice` / `maxPrice` | Keeps only listings in the price range (EUR). |
| `minYear` / `maxYear` | Keeps only listings registered in that year range. |
| `maxMileageKm` | Keeps only listings with at most this many kilometers. |
| `maxItems` | The run stops once this many listings are saved (default 50). |

## Three ways to use it

### 1. Apify console, no code

1. Open [the Actor page](https://apify.com/bibian/leboncoin-cars-scraper) and click **Try for free** (a free Apify account is enough).
2. Fill in your filters (keywords, brand, price or year range) and click **Start**.
3. When the run finishes, open the **Output** tab, check the table, then **Export** as CSV, Excel or JSON.
4. For a daily alert, open **Schedules**, create a daily schedule for the Actor and, optionally, add an integration that sends new listings to Slack, e-mail or Google Sheets.

### 2. Apify API with JavaScript

```bash
npm install apify-client
export APIFY_TOKEN="your token from Apify console, Settings, Integrations"
node examples/run.js
```

```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('bibian/leboncoin-cars-scraper').call({
    "query": "break diesel",
    "brand": "PEUGEOT",
    "maxMileageKm": 150000,
    "maxItems": 50
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(`${item.title} | ${item.price} EUR | ${item.mileageKm} km | ${item.dealerName}`);
}
```

The complete file is [`examples/run.js`](examples/run.js) (ES module, Node 18 or later).

### 3. Apify API with Python

```bash
pip install apify-client
export APIFY_TOKEN="your token from Apify console, Settings, Integrations"
python examples/run.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("bibian/leboncoin-cars-scraper").call(run_input={
    "query": "break diesel",
    "brand": "PEUGEOT",
    "maxMileageKm": 150000,
    "maxItems": 50,
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(f"{item['title']} | {item.get('price')} EUR | {item.get('mileageKm')} km | {item.get('dealerName')}")
```

The complete file is [`examples/run.py`](examples/run.py). Never put your token in the code: read it from the `APIFY_TOKEN` environment variable as above.

## Pricing

Pay per result: **$5.00 per 1,000 listings** (that is $0.005 per listing), plus a tiny start fee of $0.00005 per run. You pay only for the results saved to the dataset. Leboncoin blocks plain requests and datacenter proxies outright, so every listing needs a residential IP, which costs more per request than a typical site. Prices are those shown on the [Store page](https://apify.com/bibian/leboncoin-cars-scraper) when this guide was written; the Store page is the reference.

## Limits and honest notes

- Only professional sellers (`owner_type=pro`) are collected: the search itself is restricted, and a listing is dropped again as a safety net if it is not. No private seller's name, phone or address is ever collected.
- `dealerName` and `dealerSiren` are the dealership's public trade name and French business registration number, required by law on professional listings — never an individual's data.
- No full description is included: Leboncoin's search results carry only structured specifications (brand, model, year, mileage, fuel and more), not free-text ad copy.
- The site returns at most a few thousand listings per search. To collect more, narrow the filters (brand, price, year) or run it regularly.
- This is an unofficial tool, not affiliated with Leboncoin. Check the site terms and the data protection rules that apply to your use.

## FAQ

**Does it collect private sellers' listings?**  
No. The search is restricted to professional sellers, checked a second time on every listing before it is saved.

**Why is it more expensive than most classifieds scrapers?**  
Leboncoin blocks plain requests and datacenter proxies outright; every page needs a residential IP, which costs more per request than a typical site.

**Can I filter by brand, price or mileage?**  
Yes, with the `brand`, `minPrice`/`maxPrice`, `minYear`/`maxYear` and `maxMileageKm` input fields.

## Try it

**[Open leboncoin-cars-scraper on the Apify Store](https://apify.com/bibian/leboncoin-cars-scraper)**

The code in `examples/` is released under the MIT license (see [LICENSE](LICENSE)). The data belongs to its original publishers.
