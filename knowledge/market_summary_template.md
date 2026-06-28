# Market Summary Template

Market Intelligence reports should follow this structure.

## Market Overview

- Number of covered companies
- Sector composition
- Market momentum
- Notable news
- Event count

## Sector Analysis

For each sector:

- Ticker count
- Average score
- Average PER
- Average EPS
- Average momentum
- News count

## Market Trend

Summarize rule-based trends:

```text
Technology

Momentum
Strong

News
High

Financial Health
Good
```

## Market Psychology

Use `knowledge/market_psychology.md`.

Market psychology should be written carefully:

- Use "考えられます"
- Avoid definitive claims
- Do not imply investment advice
- Explain data limitations

## Dashboard JSON

The dashboard JSON should provide:

```json
{
  "market": {},
  "sectors": [],
  "top_events": [],
  "summary": {}
}
```
