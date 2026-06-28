# Data Model

This document summarizes the current generated data structure.

Generated data is not tracked by Git. It is created by local runs or GitHub Actions.

## prices

Path:

```text
storage/raw/prices/{ticker}.csv
```

Columns:

```text
date, open, high, low, close, volume
```

## companies

Path:

```text
storage/raw/companies/{ticker}.json
```

Main fields:

```text
ticker
company_name
sector
industry
country
currency
exchange
market_cap
enterprise_value
shares_outstanding
beta
trailing_pe
forward_pe
peg_ratio
price_to_book
eps
forward_eps
dividend_yield
52_week_high
52_week_low
average_volume
employees
website
business_summary
```

## financials

Path:

```text
storage/raw/financials/{ticker}.json
```

Main fields:

```text
ticker
currency
fiscal_year
fiscal_quarter
total_revenue
gross_profit
operating_income
net_income
ebitda
eps
diluted_eps
operating_margin
profit_margin
free_cash_flow
capital_expenditure
research_and_development
cash
total_assets
total_liabilities
shareholders_equity
long_term_debt
current_ratio
```

## news

Path:

```text
storage/raw/news/{ticker}.json
```

Main fields:

```text
ticker
title
summary
published_at
publisher
url
language
source
related_tickers
```

## events

Path:

```text
storage/events/{ticker}_events.json
```

Main fields:

```text
event_id
ticker
published_at
title
url
source
close_price
previous_close
price_change_percent
volume
```

## Scoring Reports

Path:

```text
reports/scoring/company_scores.csv
reports/scoring/company_scores.json
reports/scoring/explanations/{ticker}.md
```

Purpose:

- Store explainable company scores
- Preserve category scores, reasons, Evidence, Confidence, and used metrics
- Support future backtesting and scoring rule improvement

These generated reports are intentionally excluded from Git.

Main fields:

```text
ticker
company_name
total_score
growth_score
financial_health_score
valuation_score
momentum_score
news_score
confidence
confidence_completeness
evidence_sources
```

## Future Entity-Based Model

The current model stores data by type. A future version may move toward ticker-based entities:

```text
storage/entities/NVDA/
├── company.json
├── financials.json
├── prices.csv
└── news.json
```
