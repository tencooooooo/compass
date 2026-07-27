# 🧭 Compass

Explainable AI Investment Research Platform

`v1.0-alpha`

Compass is an AI investment research platform for US growth stocks.

This project is currently in Alpha. It is a research platform foundation, not a finished investment product.

Compass does not predict stock prices, issue buy/sell calls, set target prices, or provide investment advice. Its purpose is to collect facts, organize company information, and generate explainable research reports that help humans decide what to investigate next.

## Project Overview

Compass currently supports:

- Daily OHLCV market data collection
- Company profile collection
- Financial data collection
- News collection
- Event Database generation
- Company analysis reports
- Comparative analysis reports
- Explainable Scoring Engine
- Market Intelligence Engine
- Discovery Engine
- Backtesting & Validation Engine
- Slack Notification Engine
- Notification Engine with Slack Connector
- Memory Engine
- Feedback Engine
- Decision Engine
- Learning Engine
- Compass Workspace
- Compass API
- Compass Agent Layer
- Query Engine
- Compass MCP Server
- Time Machine Engine
- Pattern Intelligence Engine
- Theme Intelligence Engine
- Performance Evaluation Engine
- Strategy Evaluation Engine
- Experiment Engine
- Data Expansion Collector Framework
- Data Source Hub
- SEC EDGAR Integration
- Earnings Call Integration
- Human-maintained Knowledge
- GitHub Actions cloud execution
- GitHub operation documents

Generated data and reports are not tracked by Git. They are created by local runs or GitHub Actions and uploaded as workflow artifacts.

## Purpose

Compass is designed to support long-term company research.

- Collect reusable data for US stocks
- Maintain Knowledge as human-edited analysis rules and project memory
- Generate Markdown research reports
- Compare peer groups across fundamentals, financials, momentum, news, and events
- Score companies with reasons, evidence, and confidence
- Understand market and sector context before company discovery
- Discover additional research candidates without issuing investment decisions
- Validate Discovery results against later price movement
- Send a concise daily Morning Research Brief to Slack
- Send event-driven alerts only when important changes occur
- Preserve daily analysis results in a provider-based Memory Layer
- Generate Feedback reports and Knowledge update candidates for human review
- Generate Decision proposals without changing Knowledge automatically
- Generate Human Approved Learning packages from Approved proposals only
- Provide a read-only daily Research Workspace for generated reports and JSON outputs
- Provide a read-only API for Workspace, Mobile, Slack, MCP, and external AI clients
- Provide a model-independent Agent Layer for ChatGPT, Codex, Claude, Gemini, MCP, and future AI clients
- Provide a shared Query Engine for Workspace, MCP, Chat Interface, Slack Bot, and Mobile search
- Provide a thin MCP Server for ChatGPT, Claude, Codex, and future MCP clients
- Replay historical Compass analysis from a past snapshot date without future data leakage
- Extract explainable success, failure, sector, market, event, and similarity pattern candidates
- Analyze long-term investment themes across market, sector, company, Discovery, Pattern, and news context
- Evaluate Compass's own Discovery, Theme, Pattern, Confidence, Market, and Sector performance over time
- Simulate research-only virtual strategies from Discovery, Theme, Pattern, Score, Confidence, and Momentum rules
- Compare baseline and candidate Compass changes through reproducible experiments
- Prepare a disabled Collector Framework for future high-quality data source expansion
- Provide a Provider-based Data Source Hub for API, CSV, PDF, JSON, and future database inputs
- Collect SEC EDGAR primary filings and metadata before any AI interpretation layer
- Preserve earnings call transcripts and management commentary for future analysis layers
- Prepare for future ranking, backtesting, API, and deeper learning features

The guiding idea is simple: Compass should help humans understand companies, not replace human judgment.

## Brand Definition

Formal name:

```text
🧭 Compass
```

Subtitle:

```text
Explainable AI Investment Research Platform
```

Short name:

```text
Compass
```

Brand message:

```text
答えを出すAIではなく、考える方向を示すAI。
```

## Brand Architecture

```text
Compass
↓
Brand

Growth Hunter
↓
Growth stock screening engine

Research Engine
↓
Company analysis

Scoring Engine
↓
Scoring

Learning Engine
↓
AI improvement

Workspace
↓
Daily research interface

Portfolio Engine
↓
Future addition
```

Growth Hunter remains as the future growth stock screening engine name. It is no longer the whole project brand.

Growth Hunter will run on top of Market Intelligence. Compass first understands the market and sectors, then uses that context for future growth company discovery.

Recommended GitHub repository name:

```text
compass
```

Alternative:

```text
compass-platform
```

The project may later move under a GitHub Organization if multiple engines or applications are separated.

## Manifest And Philosophy

The project philosophy is documented separately so it remains visible as the codebase grows.

- [MANIFEST.md](MANIFEST.md): mission, vision, core values, prohibited uses, and long-term goal
- [PROJECT_PHILOSOPHY.md](PROJECT_PHILOSOPHY.md): why Knowledge, explainability, long-term thinking, and human review matter
- [docs/branding.md](docs/branding.md): brand concept, naming reason, future brand structure, logo image, and UI image
- [knowledge/brand_identity.md](knowledge/brand_identity.md): human-maintained brand identity notes

Core values:

- Knowledge First
- Fact First
- Human-in-the-loop
- Continuous Learning
- Explainability

Prohibited outputs:

- Definitive buy or sell calls
- Personalized investment advice
- Black-box AI conclusions
- Over-optimized short-term signals

## System Architecture

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

Details:

- [docs/architecture.md](docs/architecture.md)
- [docs/future_architecture.md](docs/future_architecture.md)
- [docs/data_model.md](docs/data_model.md)

## Roadmap

```text
Phase1 Foundation
Complete

Phase2 Intelligence
In progress

Phase3 Learning
Planned

Phase4 Compass Platform
Planned
```

`v1.0-alpha` marks the first major milestone:

- Phase1 Foundation is complete
- Phase2 Intelligence has started
- The project completed its Compass rebranding milestone
- Project philosophy, documentation, and GitHub operation foundations are organized

Version history is maintained in [CHANGELOG.md](CHANGELOG.md) and [knowledge/project_history.md](knowledge/project_history.md).

## History

```text
2026
AI Growth Hunter として開始
↓
Compassへリブランド
```

AI Growth Hunter remains in the history as the original project name. Growth Hunter remains reserved for the future growth stock screening engine.

## Folder Structure

```text
compass/
├── agents/
├── api/
├── analyzers/
├── backtests/
├── collectors/
├── config/
├── core/
├── datasources/
├── docs/
├── engines/
├── integrations/
├── knowledge/
├── lab/
├── mcp/
├── prompts/
├── reports/              # generated, ignored by Git
├── screeners/
├── storage/
│   ├── raw/              # generated, ignored by Git
│   └── events/           # generated, ignored by Git
├── tests/
├── utils/
├── workspace/
│   └── frontend/         # React read-only research workspace
├── .github/workflows/
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── MANIFEST.md
├── PROJECT_PHILOSOPHY.md
├── README.md
└── requirements.txt
```

Details: [docs/folder_structure.md](docs/folder_structure.md)

## Generated Outputs

The following are generated by scripts or GitHub Actions and are intentionally excluded from Git:

```text
logs/
storage/raw/
storage/events/
storage/notifications/
reports/
memory/
workspace/frontend/public/compass-data/
workspace/frontend/dist/
```

When GitHub Actions runs, generated outputs are uploaded as a workflow artifact named:

```text
compass-generated-outputs
```

Long-lived operational data is also persisted to the dedicated `compass-data` branch:

```text
memory/
storage/notifications/
storage/raw/{prices,companies,financials,news}/
storage/events/
storage/knowledge_graph/
reports/{discovery,scoring,market,validation}/
reports/{feedback,proposals,knowledge_updates,learning}/
reports/{performance,strategy,experiments,graph}/
```

The workflow still restores the previous GitHub Actions cache as a migration fallback, then overlays the `compass-data` branch when available. At the end of data-producing workflows, durable operational data is committed back to `compass-data` with `if: always()` so partial updates are not lost when a later step fails.

Validation reevaluates every dated snapshot in `memory/discoveries/` and merges results by Discovery date, ticker, and period. Weekly Performance, Strategy, Experiment, and Knowledge Graph jobs restore the same operational dataset and validate required inputs before generating reports. An empty scorecard is therefore treated as an input failure instead of a successful evaluation.

Feedback History is stored in `memory/feedback/feedback_history.json`, and Proposal review state is stored in `memory/decision/proposal_index.json`. Matching files under `reports/` are read-only mirrors used by Workspace and API clients.

## Local Setup

Python 3.11 or later is recommended.

```bash
pip install -r requirements.txt
pip install -e .
```

Compass Workspace is a React + TypeScript frontend.

```bash
cd workspace/frontend
npm install
npm run sync-data
npm run dev
```

React is used because the Workspace needs responsive, stateful research views across Markdown reports, JSON summaries, filters, status pills, and future API-backed data. The current implementation reads generated JSON, Markdown, and YAML from a synced static data folder. A backend API is intentionally not required yet; the data access layer is isolated so the same UI can later move from local artifacts to API, S3, or database-backed sources.

Compass API is a FastAPI read-only interface.

```bash
uvicorn api.app:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

OpenAPI JSON:

```text
http://127.0.0.1:8000/openapi.json
```

## Local Execution

Run the pipeline steps manually when developing or checking output locally.

```bash
python -m collectors.prices.fetch_prices
python -m collectors.companies.fetch_company_profiles
python -m collectors.financials.fetch_financials
python -m collectors.news.fetch_news
python -m collectors.news.build_event_database
python -m analyzers.company_analysis.generate_company_report
python -m analyzers.comparative_analysis.generate_comparison_report
python -m engines.scoring_engine.scoring_engine
python -m engines.market_intelligence.market_monitor
python -m engines.discovery.discovery_engine
python -m engines.validation.backtest_engine
python -m core.memory.memory_engine
python -m core.feedback.feedback_engine
python -m core.decision.decision_engine
python -m core.learning.learning_engine
python -m engines.notification.notification_engine --dry-run
python -m integrations.slack.slack_notifier --dry-run
```

## GitHub Actions

The workflow is defined in:

```text
.github/workflows/fetch_prices.yml
```

It runs daily at:

```text
UTC 22:00
JST 07:00
```

Execution order:

```text
API tests
↓
Price collection
↓
Company profile collection
↓
Financial data collection
↓
News collection
↓
Event database generation
↓
Company analysis report generation
↓
Comparative analysis report generation
↓
Explainable Scoring Engine
↓
Market Intelligence Engine
↓
Discovery Engine
↓
Backtesting & Validation Engine
↓
Memory Engine
↓
Feedback Engine
↓
Decision Engine
↓
Learning Engine
↓
Notification Engine
↓
Slack notification
↓
Artifact upload
```

Generated outputs are not committed to the repository. They are available from the workflow artifact.

Slack notification uses the GitHub Secret:

```text
SLACK_WEBHOOK_URL
```

If the Secret is not configured, only the Slack notification step is skipped. The workflow itself continues.

## Knowledge

`knowledge/` is human-maintained reference material. It is not model training data.

It contains:

- Brand identity
- Investment rules and philosophy
- AI design principles
- Scoring methodology
- Confidence rules
- Evidence rules
- Market intelligence
- Sector analysis rules
- Discovery engine rules
- Candidate rules
- Growth signals
- False positive patterns
- Validation rules
- Backtest methodology
- Performance metrics
- Lessons learned
- Notification policy
- Daily report definition
- Notification rules
- Alert priorities
- Event classification
- Memory architecture
- Memory schema
- Memory retention policy
- Feedback framework
- Improvement patterns
- Success patterns
- Failure patterns
- Decision process
- Review policy
- Approval guidelines
- Learning policy
- Knowledge versioning
- Human review process
- API design
- API versioning
- Integration strategy
- Agent architecture
- Context design
- Provider design
- Query language
- Query architecture
- Search strategy
- MCP architecture
- MCP tools
- MCP usage examples
- Time Machine
- Historical analysis
- Snapshot rules
- Pattern library
- Pattern confidence
- Similarity rules
- Theme library
- Theme classification
- Theme analysis rules
- Performance metrics
- Evaluation policy
- Benchmark methodology
- Accuracy definition
- Strategy library
- Portfolio metrics
- Simulation rules
- Risk management
- Experiment design
- A/B testing policy
- Evaluation framework
- Research methodology
- Data sources
- Collector guidelines
- Data quality
- Data source architecture
- API key management
- Supported data sources
- SEC data model
- Filing types
- SEC collection rules
- Earnings call structure
- Management commentary
- Transcript analysis rules
- Scoring principles
- Financial analysis rules
- News and event analysis rules
- Market psychology notes
- Company analysis guidelines
- Comparative analysis guidelines
- Peer group definitions
- Ranking principles
- Future feature notes
- Project history and decisions

Future AI analysis should refer to Knowledge as human-authored context. Update Knowledge when project rules, analysis principles, brand rules, or design decisions change.

## Prompts

Prompts are separated from Python code.

```text
prompts/company_analysis_prompt.md
prompts/comparative_analysis_prompt.md
prompts/scoring_engine_prompt.md
prompts/market_intelligence_prompt.md
prompts/validation_prompt.md
prompts/notification_prompt.md
prompts/feedback_prompt.md
prompts/decision_prompt.md
prompts/learning_prompt.md
prompts/api_prompt.md
prompts/agent_prompt.md
prompts/query_prompt.md
prompts/mcp_prompt.md
prompts/time_machine_prompt.md
prompts/pattern_prompt.md
prompts/theme_prompt.md
prompts/performance_prompt.md
prompts/strategy_prompt.md
prompts/experiment_prompt.md
```

This makes analysis behavior easier to review and update.

## Data Model

Current generated data structure:

```text
storage/raw/prices/{ticker}.csv
storage/raw/companies/{ticker}.json
storage/raw/financials/{ticker}.json
storage/raw/news/{ticker}.json
storage/raw/macro/
storage/raw/sec/
storage/raw/earnings/
storage/raw/analyst/
storage/raw/insider/
storage/raw/etf/
storage/raw/sentiment/
storage/raw/trends/
storage/raw/jobs/
storage/raw/sec/{ticker}/filings/
storage/raw/sec/{ticker}/metadata/
storage/raw/sec/{ticker}/index.json
storage/raw/earnings/{ticker}/transcripts/
storage/raw/earnings/{ticker}/metadata/
storage/raw/earnings/{ticker}/index.json
datasources/cache/
storage/events/{ticker}_events.json
reports/scoring/company_scores.csv
reports/scoring/company_scores.json
reports/scoring/explanations/{ticker}.md
reports/market/market_summary.md
reports/market/sector_summary.md
reports/market/market_dashboard.json
reports/discovery/discovery_candidates.md
reports/discovery/discovery_candidates.json
reports/discovery/candidate_details/{ticker}.md
reports/validation/validation_summary.md
reports/validation/validation_history.csv
reports/validation/validation_history.json
reports/feedback/feedback_summary.md
reports/feedback/improvement_candidates.md
reports/feedback/feedback_history.json
reports/proposals/proposal_YYYY-MM-DD.md
reports/proposals/proposal_index.json
reports/knowledge_updates/candidate_YYYY-MM-DD.md
reports/learning/learning_package_YYYY-MM-DD.md
reports/learning/learning_summary.md
reports/learning/learning_metrics.json
storage/notifications/notification_history.json
storage/notifications/state/company_scores_latest.json
storage/notifications/state/market_trends_latest.json
memory/companies/{ticker}.json
memory/sectors/{sector}.json
memory/discoveries/YYYY-MM-DD.json
memory/validations/YYYY-MM.json
memory/market/YYYY-MM-DD.json
memory/lessons/lessons.json
memory/learning/learning_history.json
memory/query/history.json
reports/timemachine/snapshot_YYYY-MM-DD.md
reports/timemachine/discovery_YYYY-MM-DD.md
reports/timemachine/market_YYYY-MM-DD.md
reports/patterns/success_patterns.md
reports/patterns/failure_patterns.md
reports/patterns/similarity_report.md
reports/patterns/pattern_summary.md
reports/themes/theme_summary.md
reports/themes/theme_ranking.md
reports/themes/theme_similarity.md
reports/themes/{Theme}.md
reports/performance/performance_summary.md
reports/performance/discovery_accuracy.md
reports/performance/benchmark_comparison.md
reports/performance/sector_accuracy.md
reports/performance/theme_accuracy.md
reports/performance/dashboard_metrics.json
memory/performance/history.json
reports/strategy/strategy_summary.md
reports/strategy/portfolio_report.md
reports/strategy/benchmark_report.md
reports/strategy/strategy_ranking.md
reports/strategy/dashboard.json
memory/strategy/strategy_history.json
reports/experiments/experiment_summary.md
reports/experiments/experiment_results.md
reports/experiments/experiment_comparison.md
reports/experiments/dashboard.json
memory/experiments/registry.json
```

Details: [docs/data_model.md](docs/data_model.md)

Future direction:

```text
storage/entities/{ticker}/company.json
storage/entities/{ticker}/financials.json
storage/entities/{ticker}/prices.csv
storage/entities/{ticker}/news.json
```

The migration is not implemented yet.

## Future Plans

Planned additions:

- Growth Hunter
- Research Engine
- Scoring Engine improvements
- Market Intelligence Engine
- Discovery Engine
- Backtesting & Validation Engine
- Slack Notification Engine
- Notification Engine
- Memory Engine
- Feedback Engine
- Decision Engine
- Learning Engine
- Compass Workspace
- Compass API
- Compass Agent Layer
- Query Engine
- Compass MCP Server
- Time Machine Engine
- Pattern Intelligence Engine
- Theme Intelligence Engine
- Performance Evaluation Engine
- Strategy Evaluation Engine
- Experiment Engine
- Data Expansion Engine
- Data Source Hub
- SEC EDGAR Integration
- Earnings Call Integration
- Portfolio Engine
- Screening
- Backtesting
- Watchlist and alerts
- Discord, Teams, LINE, Email, and Push notification connectors
- Cursor, VS Code, MCP, ChatGPT, Codex, Claude, Gemini, and external AI integration
- Better event and market psychology analysis
- Entity-based storage model

## Engine Documentation

エンジンごとの入出力・設定・実行方法は、レイヤー単位で分割しています。

| Layer | Engines | Document |
| --- | --- | --- |
| Research Engines | Explainable Scoring Engine, Market Intelligence Engine, Discovery Engine, Backtesting & Validation Engine, Slack Notification Engine, Notification Engine | [docs/engines/research.md](docs/engines/research.md) |
| Core Engines | Memory Engine, Feedback Engine, Decision Engine, Learning Engine | [docs/engines/core.md](docs/engines/core.md) |
| Platform Layer | Compass Workspace, Compass API, Compass Agent Layer, Query Engine, Compass MCP Server | [docs/engines/platform.md](docs/engines/platform.md) |
| Lab Engines | Time Machine Engine, Pattern Intelligence Engine, Theme Intelligence Engine, Performance Evaluation Engine, Strategy Evaluation Engine, Experiment Engine, Knowledge Graph Engine | [docs/engines/lab.md](docs/engines/lab.md) |
| Foundation Layer | Data Expansion Engine, Data Source Hub, SEC EDGAR Integration, Earnings Call Integration, Data Quality Engine | [docs/engines/foundation.md](docs/engines/foundation.md) |
| Research Notebook | Research Notebook | [docs/engines/research_notebook.md](docs/engines/research_notebook.md) |

## Git Tag And Release Preparation

Recommended Git tag for this milestone:

```bash
git tag v1.0-alpha
git push origin v1.0-alpha
```

Do not create the tag until the repository contents have been reviewed and committed.

Suggested GitHub Release steps:

1. Open the repository on GitHub.
2. Go to `Releases`.
3. Select `Draft a new release`.
4. Choose the `v1.0-alpha` tag.
5. Use `Compass v1.0-alpha` as the release title.
6. Summarize that Phase1 Foundation is complete, Phase2 Intelligence has started, and the Compass rebranding milestone is complete.
7. Note that the project is Alpha and not investment advice.

## GitHub Publication Checklist

Before publishing or pushing:

- No API keys are included
- `.env` is ignored
- `.venv/` is ignored
- `logs/` is ignored
- `storage/raw/` is ignored
- `storage/events/` is ignored
- `storage/notifications/` is ignored
- `reports/` is ignored
- `memory/` is ignored
- GitHub Actions workflow is present
- `LICENSE` is present
- `README.md` is current
- `CHANGELOG.md` is current
- `CONTRIBUTING.md` is present
- `MANIFEST.md` is present
- `PROJECT_PHILOSOPHY.md` is present
- Brand name is consistently Compass

## License

This project is released under the MIT License. See [LICENSE](LICENSE).

## Disclaimer

Compass is a research support tool. It does not guarantee investment results and does not provide investment advice. Final investment decisions are the responsibility of the user.
