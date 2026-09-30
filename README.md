# Amazon Scraper

A clean web UI on top of a free, self-hosted Amazon scraper. Search products, browse best sellers and deals, and open full product details, all served from one small Python app. No API key and no call limits.

**Live demo:** https://amazon-scraper-lggp.onrender.com/

Created by **Atul Senapati**.

## Features

- **Search** with sorting, live autocomplete and paging
- **Best sellers** in 10 categories: best sellers, new releases, movers & shakers, most wished for
- **Deals** with discount and price sorting
- **Product details**: images, price, stock, seller, customer summary, highlights, rating breakdown, reviews and specs
- Paste an **ASIN or Amazon link** into the search box to open a product directly
- 8 marketplaces: US, UK, DE, FR, IN, CA, IT, ES
- Grid size switch (L / M / S), responsive down to phone width

## Run locally

Requires Python 3.10 to 3.12.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python serve.py
```

Open http://localhost:8000/. Use another port with `PORT=8010 .venv/bin/python serve.py`.

## Deploy on Render

1. Push this repo to GitHub.
2. In Render, choose **New → Blueprint** and select the repo.
3. Render reads `render.yaml`, builds the `Dockerfile` and starts the app on the free plan.

The free plan sleeps when idle, so the first request after a quiet spell can take up to a minute. Amazon may block some cloud IPs; if that happens, set an `AMAZON_PROXY` environment variable (for example `http://user:pass@host:port`).

## API

The same server exposes the scraper's JSON API, for example:

```bash
curl "http://localhost:8000/search?query=standing%20desk"
curl "http://localhost:8000/products/details?product=B07QSFHT27"
curl "http://localhost:8000/best-sellers?category=electronics"
curl "http://localhost:8000/deals"
```

Every endpoint takes an optional `country` parameter (`US`, `GB`, `DE`, ...). `GET /health` lists all available endpoints.

## Project layout

| Path | Purpose |
|---|---|
| `frontend/` | The web UI (`index.html`, `favicon.svg`) |
| `serve.py` | Starts the API and the UI on one port |
| `routes.py`, `amazon/` | The scraper and its API routes |
| `Dockerfile`, `render.yaml` | Deployment |

## Credits

The scraping engine and API come from [omkarcloud/amazon-scraper](https://github.com/omkarcloud/amazon-scraper) (see `LICENSE`). The frontend, logo and deployment setup are by Atul Senapati.

Scraping Amazon may be restricted by its terms of service. Use it responsibly and at your own risk.
