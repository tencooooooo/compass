# Foundation Layer

データソースの追加と品質保証を担当する基盤層です。分析ロジックより下に位置します。

[← README に戻る](../../README.md)

## Data Expansion Engine

Compass Foundation 2 adds a disabled Collector Framework for future data-source expansion.

Files:

```text
collectors/data_expansion.py
collectors/macro/collector.py
collectors/sec/collector.py
collectors/earnings/collector.py
collectors/analyst/collector.py
collectors/insider/collector.py
collectors/etf/collector.py
collectors/sentiment/collector.py
collectors/trends/collector.py
collectors/jobs/collector.py
```

Common interface:

```python
collect()
validate()
normalize()
save()
```

Planned data categories:

```text
Macro: CPI, FOMC, employment, interest rates, VIX
SEC: 10-K, 10-Q, 8-K
Earnings: earnings presentations, guidance
Analyst: consensus, EPS estimates
Insider: insider buying, insider selling
ETF: fund flows, holdings weight
Sentiment: Reddit, X, news sentiment
Trends: Google Trends
Jobs: hiring trends and job postings
```

Future storage:

```text
storage/raw/macro/
storage/raw/sec/
storage/raw/earnings/
storage/raw/analyst/
storage/raw/insider/
storage/raw/etf/
storage/raw/sentiment/
storage/raw/trends/
storage/raw/jobs/
```

Current state:

```text
Collectors are scaffolded only.
Collectors are disabled by default.
No external API connection is implemented.
No API key is required.
GitHub Actions does not run these collectors yet.
```

The goal is to improve Compass by improving evidence quality. New collectors should be enabled only after source quality, licensing, cost, rate limits, schema, and retention have been reviewed.

## Data Source Hub

Compass Foundation 03 adds a Provider-based Data Source Hub.

Files:

```text
datasources/base/datasource.py
datasources/base/datasource_manager.py
datasources/base/datasource_registry.py
datasources/providers/yahoo_finance/
datasources/providers/sec/
datasources/providers/fred/
datasources/providers/finnhub/
datasources/providers/alpha_vantage/
datasources/providers/csv/
datasources/providers/pdf/
datasources/providers/json/
datasources/models/
datasources/cache/
```

Configuration:

```text
config/datasources.yaml
```

Common Provider interface:

```python
connect()
fetch()
normalize()
validate()
cache()
disconnect()
```

Manager example:

```python
from datasources.base import DataSourceManager

manager = DataSourceManager()
sec = manager.get("sec")
csv_provider = manager.get("csv")
```

Registry operations:

```python
register()
unregister()
list()
exists()
```

Initial providers:

```text
Yahoo Finance: enabled, connected to existing local Compass collector outputs
SEC: enabled, SEC EDGAR filings provider
Earnings: enabled, earnings call transcript provider
CSV: enabled, local CSV reader
JSON: enabled, local JSON and Memory reader
FRED: scaffold
Finnhub: scaffold
Alpha Vantage: scaffold
PDF: scaffold for future IR material parsing
```

API Key management:

```text
GitHub Secrets
.env
Runtime environment variables
```

API keys are never stored in code. Provider configuration stores only environment variable names, such as `FRED_API_KEY`, `FINNHUB_API_KEY`, and `ALPHA_VANTAGE_API_KEY`.

Data Source Hub exists so Compass Core does not need to know whether data came from an API, CSV, PDF, JSON, or future database. New data sources should be added by registering Providers, not by changing analyzers or engines.

## SEC EDGAR Integration

Compass Foundation 04 connects the first official primary data source: SEC EDGAR.

Files:

```text
collectors/sec/fetch_filings.py
collectors/sec/sec_client.py
collectors/sec/sec_parser.py
collectors/sec/sec_normalizer.py
collectors/sec/filing_index.py
datasources/providers/sec/provider.py
```

Supported forms:

```text
10-K
10-Q
8-K
```

Future forms:

```text
DEF 14A
S-1
Form 4
```

Run locally:

```bash
python -m collectors.sec.fetch_filings --ticker NVDA --limit 1
```

Storage:

```text
storage/raw/sec/{ticker}/
  filings/
  metadata/
  index.json
```

Metadata:

```text
ticker
company_name
filing_type
filing_date
accession_number
source_url
document_title
```

Rate limit policy:

```text
User-Agent is declared on every request.
Default request interval is 0.2 seconds.
Retries are used for transient HTTP or network failures.
Duplicate accession numbers are skipped when already saved.
```

SEC User-Agent can be provided through:

```text
SEC_USER_AGENT
```

GitHub Actions:

```text
.github/workflows/fetch_sec_filings.yml
```

This workflow is independent from the daily market data pipeline and uploads SEC artifacts separately.

SEC filings are stored as facts. AI summarization, risk extraction, and financial statement interpretation will be implemented in a later layer.

## Earnings Call Integration

Compass Foundation 05 adds earnings call transcript collection.

Files:

```text
collectors/earnings/fetch_transcripts.py
collectors/earnings/transcript_client.py
collectors/earnings/transcript_parser.py
collectors/earnings/transcript_normalizer.py
collectors/earnings/transcript_index.py
datasources/providers/earnings/provider.py
```

Run locally:

```bash
python -m collectors.earnings.fetch_transcripts --ticker NVDA --source-path path/to/transcript.txt --fiscal-quarter "FY2026 Q1"
```

Storage:

```text
storage/raw/earnings/{ticker}/
  transcripts/
  metadata/
  index.json
```

Transcript metadata:

```text
ticker
company_name
fiscal_quarter
earnings_date
transcript_date
source
language
participants
ceo_name
cfo_name
```

Transcript structure:

```text
paragraphs
opening_remarks
financial_highlights
guidance
qa_section
closing_remarks
```

Data Source Hub:

```text
manager.get("earnings")
```

GitHub Actions:

```text
.github/workflows/fetch_earnings_transcripts.yml
```

The workflow is independent from existing collectors. It accepts a ticker and transcript source path or future source URL, then uploads generated transcript artifacts.

Earnings transcripts are preserved as management commentary. AI summarization, sentiment scoring, credibility assessment, and investment interpretation are planned for later layers.

## Data Quality Engine

Compass Foundation 06 adds a Data Quality Engine that evaluates input data before analysis begins.

Files:

```text
foundation/data_quality/quality_engine.py
foundation/data_quality/quality_checker.py
foundation/data_quality/freshness_checker.py
foundation/data_quality/duplicate_detector.py
foundation/data_quality/reliability_scorer.py
foundation/data_quality/quality_report.py
```

Run locally:

```bash
python -m foundation.data_quality.quality_engine
```

Evaluation targets:

```text
Prices
Companies
Financials
News
Events
SEC
Earnings
Macro
ETF
Insider
Analyst
Trends
Future Providers
```

Quality Score:

```text
Freshness
Completeness
Reliability
Duplicate risk
Consistency
```

Outputs:

```text
storage/quality/provider_scores.json
storage/quality/history.json
storage/quality/issues.json
reports/data_quality/quality_summary.md
reports/data_quality/provider_ranking.md
reports/data_quality/detected_issues.md
reports/data_quality/dashboard.json
```

GitHub Actions:

```text
.github/workflows/fetch_prices.yml
```

The daily workflow runs Data Quality after collectors finish and before analysis starts. If the overall Quality Score is below the configured threshold, the workflow emits a warning but does not stop.
