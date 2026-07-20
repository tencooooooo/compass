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
signal_strength
signal_rate
evidence_sources
```

## Market Reports

Path:

```text
reports/market/market_summary.md
reports/market/sector_summary.md
reports/market/market_dashboard.json
```

Purpose:

- Store market and sector summaries
- Preserve dashboard-ready market structure
- Support future Growth Hunter screening

Dashboard JSON structure:

```json
{
  "market": {},
  "sectors": [],
  "top_events": [],
  "summary": {}
}
```

## Discovery Reports

Path:

```text
reports/discovery/discovery_candidates.md
reports/discovery/discovery_candidates.json
reports/discovery/candidate_details/{ticker}.md
```

Purpose:

- Store additional research candidates
- Preserve Discovery Score, reasons, watch points, Confidence, and Evidence
- Provide the foundation for future Growth Hunter screening

## Validation Reports

Path:

```text
reports/validation/validation_summary.md
reports/validation/validation_history.csv
reports/validation/validation_history.json
```

Purpose:

- Compare Discovery candidates with later price performance
- Store validation results for 1w, 1m, 3m, 6m, and 1y periods
- Preserve Return, benchmark difference, sector difference, Confidence, and completion status
- Provide the foundation for the future Learning Engine

Main fields:

```text
discovery_date
validation_date
period
ticker
discovery_score
discovery_reasons
start_date
end_date
start_price
end_price
validation_result
return_percent
benchmark
benchmark_return_percent
benchmark_diff_percent
sector_average_return_percent
sector_diff_percent
confidence
signal_strength
event_count
evidence
period_complete
```

## Notification History

Path:

```text
storage/notifications/notification_history.json
storage/notifications/state/company_scores_latest.json
storage/notifications/state/market_trends_latest.json
```

Purpose:

- Store event-driven notification history
- Prevent duplicate notifications
- Preserve previous score and market trend snapshots for next-run comparison
- Support future notification connectors such as Discord, Teams, LINE, Email, and Push

Main fields:

```text
event_id
event_type
priority
title
ticker
detected_at
recorded_at
channel
status
error
```

## Memory

Path:

```text
memory/companies/{ticker}.json
memory/sectors/{sector}.json
memory/discoveries/YYYY-MM-DD.json
memory/validations/YYYY-MM.json
memory/market/YYYY-MM-DD.json
memory/lessons/lessons.json
```

Purpose:

- Store long-term daily analysis snapshots
- Preserve company, sector, discovery, validation, market, and lessons history
- Provide future Learning Engine input
- Allow future provider migration from Local JSON to S3 or Database

Provider API:

```text
save
load
update
delete
exists
list
search
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
