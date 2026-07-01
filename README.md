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
├── api/
├── analyzers/
├── backtests/
├── collectors/
├── config/
├── core/
├── docs/
├── engines/
├── integrations/
├── knowledge/
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

## Local Setup

Python 3.11 or later is recommended.

```bash
pip install -r requirements.txt
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
python collectors/prices/fetch_prices.py
python collectors/companies/fetch_company_profiles.py
python collectors/financials/fetch_financials.py
python collectors/news/fetch_news.py
python collectors/news/build_event_database.py
python analyzers/company_analysis/generate_company_report.py
python analyzers/comparative_analysis/generate_comparison_report.py
python engines/scoring_engine/scoring_engine.py
python engines/market_intelligence/market_monitor.py
python engines/discovery/discovery_engine.py
python engines/validation/backtest_engine.py
python core/memory/memory_engine.py
python core/feedback/feedback_engine.py
python core/decision/decision_engine.py
python core/learning/learning_engine.py
python engines/notification/notification_engine.py --dry-run
python integrations/slack/slack_notifier.py --dry-run
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
```

This makes analysis behavior easier to review and update.

## Data Model

Current generated data structure:

```text
storage/raw/prices/{ticker}.csv
storage/raw/companies/{ticker}.json
storage/raw/financials/{ticker}.json
storage/raw/news/{ticker}.json
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
- Portfolio Engine
- Screening
- Backtesting
- Watchlist and alerts
- Discord, Teams, LINE, Email, and Push notification connectors
- API
- LLM integration
- Better event and market psychology analysis
- Entity-based storage model

## Explainable Scoring Engine

Compass Research 01 adds an Explainable Scoring Engine.

Output:

```text
reports/scoring/company_scores.csv
reports/scoring/company_scores.json
reports/scoring/explanations/{ticker}.md
```

The score is 100 points total:

```text
Growth: 20
Financial Health: 20
Valuation: 20
Momentum: 20
News: 20
```

Each score includes:

- Reason
- Evidence
- Used metrics
- Missing data
- Confidence

Confidence is one of:

```text
High
Medium
Low
```

The score is not a ranking or investment decision. It is an evidence-based research aid. A high score with low confidence must be reviewed carefully.

## Market Intelligence Engine

Compass Research 02 adds a Market Intelligence Engine.

Output:

```text
reports/market/market_summary.md
reports/market/sector_summary.md
reports/market/market_dashboard.json
```

It summarizes:

- Covered company count
- Sector composition
- Market momentum
- Notable news
- Event count
- Sector averages
- Rule-based market trends
- Rule-based market psychology

Market Intelligence does not generate company rankings. It builds the market and sector context that future Growth Hunter screening will use.

## Discovery Engine

Compass Research 03 adds a Discovery Engine.

Output:

```text
reports/discovery/discovery_candidates.md
reports/discovery/discovery_candidates.json
reports/discovery/candidate_details/{ticker}.md
```

Discovery Engine uses:

- Price
- Company
- Financials
- News
- Events
- Company Analysis
- Comparative Analysis
- Scoring Engine
- Market Intelligence
- Knowledge

It does not generate investment rankings. It identifies companies that may deserve additional research and explains why.

Discovery Engine is the foundation for the future Growth Hunter engine.

## Backtesting & Validation Engine

Compass Research 04 adds a Backtesting & Validation Engine.

Output:

```text
reports/validation/validation_summary.md
reports/validation/validation_history.csv
reports/validation/validation_history.json
```

Validation Engine checks Discovery candidates against stored price history for:

```text
1w
1m
3m
6m
1y
```

It records:

- Discovery date
- Discovery Score
- Discovery reasons
- Start price
- End price
- Return
- Benchmark difference when benchmark data exists
- Sector difference when peer data exists
- Validation result
- Confidence

Validation result labels:

```text
Excellent
Good
Neutral
Poor
```

Periods that are not complete yet are kept as `Neutral` and marked as incomplete. This avoids pretending that Compass has evidence before enough time has passed.

Validation is the foundation for the future Learning Engine. It stores what happened after Discovery so humans can later review whether Scoring and Discovery rules should be improved. It does not perform automatic learning yet.

## Slack Notification Engine

Compass Research 05 adds a Slack Notification Engine.

Files:

```text
integrations/slack/slack_notifier.py
integrations/slack/slack_formatter.py
config/notification.yaml
```

GitHub Secret:

```text
SLACK_WEBHOOK_URL
```

To configure Slack:

1. Create a Slack Incoming Webhook in your Slack workspace.
2. Copy the webhook URL.
3. Open the GitHub repository settings.
4. Go to `Settings > Secrets and variables > Actions`.
5. Add a repository secret named `SLACK_WEBHOOK_URL`.

Success notification:

- Execution timestamp
- Success status
- Covered ticker count
- Discovery candidate count
- Top candidates with Discovery Score and Confidence
- Score changes when previous score data is available
- Market Intelligence sector summary
- Important news titles
- Validation result counts
- Artifact name

Failure notification:

- Failed workflow status
- Step hint
- Error hint
- Timestamp
- GitHub Actions run number

Slack notifications are intentionally brief. They are a Morning Research Brief, not a replacement for generated reports. Detailed analysis remains in the Markdown, CSV, and JSON artifacts.

## Notification Engine

Compass Research 06 adds an event-driven Notification Engine.

Files:

```text
engines/notification/notification_engine.py
engines/notification/event_detector.py
engines/notification/notification_router.py
integrations/slack/slack_connector.py
```

Notification Engine detects:

- Discovery Alert: Discovery Score 90 or higher
- Score Change Alert: score changed by 5 points or more
- Market Trend Alert: Market Intelligence sector trend changed
- Important News Alert: important news categories from `knowledge/news_analysis_rules.md`
- Validation Alert: Validation result became Excellent
- Workflow Failure: GitHub Actions failure

Notifications are routed through `NotificationRouter`. Slack is the first connector. Future connectors can be added for:

```text
Discord
Teams
LINE
Email
Push notification
```

Event history is saved to:

```text
storage/notifications/notification_history.json
```

The workflow restores `storage/notifications/` through GitHub Actions cache so Score Change and Market Trend alerts can compare with the previous run. The folder is ignored by Git and uploaded as part of the generated artifact.

Notification Engine is intentionally selective. It sends alerts for action-worthy changes, not every data point.

## Memory Engine

Compass Core 01 adds a provider-based Memory Layer.

Files:

```text
core/memory/memory_engine.py
core/memory/memory_provider.py
core/memory/local_provider.py
```

Memory API:

```text
Memory.save()
Memory.load()
Memory.update()
Memory.delete()
Memory.exists()
Memory.list()
Memory.search()
```

Current provider:

```text
LocalProvider
```

Future providers:

```text
S3Provider
PostgresProvider
SupabaseProvider
```

Current local output:

```text
memory/companies/
memory/sectors/
memory/discoveries/
memory/validations/
memory/market/
memory/lessons/
```

`memory/` is ignored by Git, restored through GitHub Actions cache, and included in workflow artifacts. This keeps Memory as operational data while allowing future migration to S3 or a database without changing Analyzer or Engine callers.

## Feedback Engine

Compass Core 02 adds a Feedback Layer.

Files:

```text
core/feedback/feedback_engine.py
core/feedback/feedback_analyzer.py
core/feedback/improvement_detector.py
```

Output:

```text
reports/feedback/feedback_summary.md
reports/feedback/improvement_candidates.md
reports/feedback/feedback_history.json
```

Feedback Engine compares Discovery results with Validation results and summarizes:

- Discovery Accuracy
- Score Accuracy
- Confidence Accuracy
- Sector Accuracy
- Event Accuracy
- Success patterns
- Failure patterns

Feedback Engine is not the Learning Engine. It does not automatically update Knowledge, scoring rules, or investment rules.

Its role is to generate Knowledge update candidates for human review. Learning Engine should be built later on top of accumulated Feedback History and reviewed Knowledge changes.

## Decision Engine

Compass Core 03 adds a Decision Layer.

Files:

```text
core/decision/decision_engine.py
core/decision/proposal_generator.py
core/decision/review_manager.py
```

Output:

```text
reports/proposals/proposal_YYYY-MM-DD.md
reports/proposals/proposal_index.json
reports/knowledge_updates/candidate_YYYY-MM-DD.md
```

Decision Engine converts Feedback improvement candidates into human-reviewable proposals. Each proposal includes:

- Proposal ID
- Target
- Reason
- Evidence
- Impact scope
- Expected effect
- Risk
- Recommendation
- Approve / Reject / Review Later options

Proposal status is tracked in JSON with:

```text
Pending
Approved
Rejected
Deferred
```

Decision Engine protects Knowledge. It generates proposal and Knowledge update candidate files, but it does not change Knowledge, Scoring, Rules, or prompts automatically.

## Learning Engine

Compass Core 04 adds a Human Approved Learning Layer.

Files:

```text
core/learning/learning_engine.py
core/learning/proposal_loader.py
core/learning/learning_package_builder.py
core/learning/learning_history.py
```

Output:

```text
reports/learning/learning_package_YYYY-MM-DD.md
reports/learning/learning_summary.md
reports/learning/learning_metrics.json
memory/learning/learning_history.json
```

Knowledge version templates:

```text
knowledge/versions/v1.json
knowledge/versions/v2.json
```

Learning Engine only loads proposals with:

```text
Approved
```

Rejected, Deferred, and Pending proposals are ignored.

Learning Engine does not rewrite Knowledge, Scoring, Rules, or prompts. It builds a Learning Package that summarizes approved proposals, adoption reasons, expected effects, impact scope, Knowledge candidates, Scoring candidates, and review history.

This keeps Compass explainable, traceable, and rollbackable. Knowledge changes remain human-owned.

## Compass Workspace

Compass Experience 01 adds a read-only Research Workspace for daily use.

Files:

```text
workspace/frontend/
workspace/frontend/src/components/
workspace/frontend/src/pages/
workspace/frontend/src/services/
workspace/frontend/src/types/
workspace/frontend/scripts/sync-data.mjs
```

Pages:

```text
Home
Discovery
Company
Comparison
Validation
Proposal
Learning
Settings
```

Workspace reads generated artifacts from:

```text
reports/
storage/notifications/
memory/learning/
config/
```

`npm run sync-data` copies those files into `workspace/frontend/public/compass-data/` for local Vite serving. That copied folder is ignored by Git because it contains generated operational data.

The Workspace is not a trading dashboard. It is designed as the first screen a researcher opens in the morning: concise summary, discovery candidates, market context, validation evidence, proposals, and learning packages in one place. Editing, approvals, and Knowledge updates remain outside the UI for now.

Future direction:

```text
Local static artifacts
↓
Backend API
↓
S3 / Database / Cloud Storage
```

The frontend service layer keeps that migration path open without requiring page components to know where Compass data is stored.

## Compass API

Compass Platform 01 adds a read-only FastAPI layer.

Files:

```text
api/app.py
api/routes/
api/services/
api/models/
api/schemas/
tests/api/
```

Version prefix:

```text
/api/v1/
```

Endpoints:

```text
GET /api/v1/companies
GET /api/v1/companies/{ticker}
GET /api/v1/discovery
GET /api/v1/discovery/top
GET /api/v1/scores
GET /api/v1/scores/{ticker}
GET /api/v1/market
GET /api/v1/market/sectors
GET /api/v1/validation
GET /api/v1/validation/{ticker}
GET /api/v1/proposals
GET /api/v1/learning
GET /api/v1/notifications
```

All endpoints return JSON through a unified envelope:

```json
{
  "success": true,
  "data": {},
  "timestamp": "",
  "version": "v1"
}
```

Swagger UI is enabled at:

```text
/docs
```

OpenAPI JSON is available at:

```text
/openapi.json
```

The API currently reads local generated artifacts and does not require authentication. Future authentication can add API Key, JWT, or OAuth without changing the response envelope.

Future clients:

```text
Workspace
Mobile
Slack Bot
MCP
External AI
```

The API is intended to become the only public data interface for Compass, so clients do not need to understand local Markdown, JSON, CSV, or future storage layouts.

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
