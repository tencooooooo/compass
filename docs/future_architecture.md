# Future Architecture

Compass will grow from a data collection and reporting project into a broader research platform.

## Target Flow

```text
Collectors
    ↓
Storage
    ↓
Knowledge
    ↓
Analysis
    ↓
Scoring
    ↓
Market Intelligence
    ↓
Discovery
    ↓
Learning
    ↓
Dashboard
    ↓
API
```

## Layers

### Collectors

Collectors gather factual data such as prices, company profiles, financials, news, and future data sources.

### Storage

Storage keeps raw and processed data in predictable formats. The current structure is source-based, while the future direction is entity-based storage by ticker.

### Knowledge

Knowledge stores human-written rules, definitions, principles, and project memory. It guides AI behavior and keeps assumptions visible.

### Analysis

Analyzers generate company and comparative reports from stored data and Knowledge.

### Scoring

Future scoring will organize research priority using explainable criteria. It must not become a black-box buy or sell system.

### Learning

Learning features may use historical outcomes, event patterns, and reviewed reports to improve research quality.

### Dashboard

The dashboard will make reports, watchlists, rankings, and alerts easier to review.

### API

An API layer may expose collected data, reports, and research signals to other tools.

## Design Direction

The architecture should remain modular. New collectors, analyzers, screeners, and interfaces should be added without breaking existing outputs.

## Brand Direction

Future modules should fit the Compass brand architecture:

- Research Engine: company analysis
- Growth Hunter: growth stock screening
- Scoring Engine: scoring and ranking
- Market Intelligence Engine: market, sector, and market psychology context
- Discovery Engine: additional research candidate discovery
- Learning Engine: AI improvement
- Portfolio Engine: future portfolio research support
- Dashboard: future user interface
- API: future integration layer
