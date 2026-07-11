# Changelog

## v1.0-alpha

- Fixed durable Validation tracking: each daily run now reevaluates all Discovery Memory snapshots, merges prior monthly Validation rows, and partitions the ledger by Discovery month so 1w/1m/3m/6m/1y outcomes can mature across runners.
- Expanded `compass-data` persistence to include the minimal raw data and generated reports required by weekly Performance, Strategy, Experiment, and Knowledge Graph jobs. Scheduled jobs now fail clearly when restored inputs are empty.
- Made Feedback History and Proposal Review state durable under `memory/`, with report JSON mirrors for Workspace and API readers. Approved review state now survives daily runners and remains available to Learning.
- Added deduplicated News and Event histories to Company Memory. Important-news alerts now require a high-signal pattern within 36 hours, and the daily pipeline runs on weekdays.
- Changed Performance Evaluation to evaluate all durable Discovery snapshots instead of only the latest report.
- Changed Momentum scoring: each window (1M/3M/6M/1Y) is now scored on the excess return versus the SPY benchmark when benchmark prices are available, with absolute-return fallback recorded in missing data. This separates stock-specific strength from market-wide direction.
- Changed Discovery momentum: candidate momentum now uses the same benchmark-relative excess-return rule as the Scoring Engine, keeping Discovery Score consistent with scoring signals.
- Changed Growth scoring: revenue and EPS YoY growth are now averaged across up to the latest four quarters with prior-year comparisons to reduce single-quarter noise, with acceleration and deceleration noted in reasons.
- Changed News scoring: sentiment now uses the net ratio of positive minus negative items over classified items instead of raw count differences, removing the coverage-volume bias toward heavily reported companies.

- Added benchmark price collection: `config/tickers.yaml` now defines a `benchmarks` list (SPY and sector ETFs) collected for prices only, enabling the previously inactive benchmark comparison in validation.
- Changed Event Database news attribution: news published after the US market close (16:00 ET) is now attributed to the next trading day so event price reactions measure the correct session.
- Added news deduplication: syndicated duplicates are removed at collection and before News scoring so coverage points are not inflated.
- Added SEC vs yfinance revenue cross-check: quarterly revenue gaps above 10 percent are recorded as `quarterly_cross_check` data quality warnings.
- Added SEC EDGAR quarterly financials enrichment: XBRL companyfacts now replace yfinance quarterly time series when at least five quarters are available, with the yfinance series preserved as a fallback reference.
- Added OHLCV validation on price collection: contradictory rows (negative prices, high below low, negative volume) are dropped with warnings, and extreme daily moves are flagged for review.
- Changed Scoring methodology: Growth now uses quarterly revenue and EPS YoY growth when available, with latest-value fallback when time series data is missing.
- Changed News scoring: sentiment keyword classification is centralized with word-boundary matching, phrase overrides, negation handling, and labeled accuracy tests.
- Changed Valuation scoring: PER, Forward PER, PEG, and PBR now prefer sector-relative percentile scoring when at least five sector peers are available.
- Added Discovery universe recording and Performance confidence-level validation result distribution. These scoring changes intentionally break direct continuity with older generated score reports.
- Marked the first Alpha milestone for Compass.
- Documented Phase1 Foundation as complete and Phase2 Intelligence as started.
- Added `MANIFEST.md` and `PROJECT_PHILOSOPHY.md`.
- Added future architecture, development principles, and release strategy documentation.
- Added Knowledge files for investment philosophy, AI design principles, and future features.
- Project Rebranding: AI Growth Hunter was rebranded to Compass.
- Reserved Growth Hunter as the future growth stock screening engine name.
- Added Compass Research 01: Explainable Scoring Engine with score explanations, confidence, and evidence.
- Added Compass Research 02: Market Intelligence Engine with market summary, sector summary, and dashboard JSON.
- Added Compass Research 03: Discovery Engine for explainable additional research candidate discovery.
- Added Compass Research 04: Backtesting & Validation Engine with validation summary, history tracking, and Learning Engine foundation.
- Added Compass Research 05: Slack Notification Engine for Daily Research Brief and failure notifications.
- Added Compass Research 06: Notification Engine with event detection, routing, Slack Connector, and notification history.
- Added Compass Core 01: Memory Engine with provider interface, LocalProvider, and local JSON memory.
- Added Compass Core 02: Feedback Engine with feedback summary, improvement candidates, and feedback history.
- Added Compass Core 03: Decision Engine with proposal generation, proposal index, review status management, and Knowledge update candidates.
- Added Compass Core 04: Learning Engine with Human Approved Learning packages, learning history, learning metrics, and Knowledge version templates.

```text
AI Growth Hunter
↓
Compass
```

## v0.7.1

- Prepared the project for GitHub-based long-term operation.
- Added `.gitignore`, MIT `LICENSE`, `CONTRIBUTING.md`, and `docs/`.
- Clarified generated data and reports are not tracked by Git.

## v0.7

- Added comparative analysis reports.
- Added peer group comparison for market overview, mega tech, semiconductor, and technology sector.

## v0.6

- Added company analysis report generation.
- Added prompt separation and company analysis Knowledge files.

## v0.5

- Added news collection.
- Added Event Database linking news to price and volume facts.

## v0.4

- Added financial data collection.
- Added data model direction notes.

## v0.3

- Added company profile collection.
- Added the Knowledge directory.

## v0.2

- Refactored project structure for long-term operation.
- Added settings, logging, collectors, and storage structure.

## v0.1

- Added daily OHLCV market data collection.
- Added GitHub Actions workflow foundation.
