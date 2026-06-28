# Architecture

Compass is organized as a data and intelligence pipeline.

```text
Collectors
    ↓
Storage
    ↓
Knowledge
    ↓
Analyzers
    ↓
Engines
    ↓
Reports
```

## Collectors

Collectors retrieve factual data from external sources.

- `collectors/prices/`: Daily OHLCV price data
- `collectors/companies/`: Company profile data
- `collectors/financials/`: Financial statement data
- `collectors/news/`: News data and event database generation

## Storage

Runtime data is written under `storage/`.

- `storage/raw/prices/`
- `storage/raw/companies/`
- `storage/raw/financials/`
- `storage/raw/news/`
- `storage/events/`

These generated folders are intentionally excluded from Git.

## Knowledge

`knowledge/` stores human-maintained analysis rules, terminology, roadmap notes, and design decisions. It is reference material for analysis, not model training data.

## Analyzers

Analyzers read stored data and Knowledge to produce Markdown reports.

- `analyzers/company_analysis/`
- `analyzers/comparative_analysis/`

## Engines

Engines convert stored facts into explainable research signals.

- `engines/scoring_engine/`: Explainable scoring with reasons, evidence, and confidence
- `engines/market_intelligence/`: Market and sector context reports
- `engines/discovery/`: Additional research candidate discovery

## Reports

Generated reports are written under `reports/`. Reports are runtime outputs and are intentionally excluded from Git.

## Future Direction

The future architecture is documented in [future_architecture.md](future_architecture.md).
