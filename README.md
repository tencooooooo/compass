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

## Compass Agent Layer

Compass Platform 02 adds a model-independent Agent Layer.

Files:

```text
agents/base_agent.py
agents/context_builder.py
agents/prompt_manager.py
agents/research_agent.py
agents/discovery_agent.py
agents/market_agent.py
agents/portfolio_agent.py
agents/providers/
```

Agent lifecycle:

```text
load_data()
↓
prepare_context()
↓
build_prompt()
↓
provider.generate()
↓
format_response()
```

Current agents:

```text
ResearchAgent
DiscoveryAgent
MarketAgent
PortfolioAgent
```

`PortfolioAgent` is a placeholder. It does not make portfolio decisions.

Current provider:

```text
DummyProvider
```

Future providers:

```text
OpenAIProvider
ClaudeProvider
GeminiProvider
MCPProvider
```

Agent Layer uses Compass API-facing services and normalized context objects. It does not update Knowledge, Memory, reports, scoring rules, or prompts.

Future clients:

```text
MCP
ChatGPT
Codex
Claude
Gemini
Slack Bot
External AI Agents
```

The design goal is Compass-centered architecture: AI models can change, but Compass remains the research platform and source of truth.

## Query Engine

Compass Platform 03 adds a shared internal Query Engine.

Files:

```text
engines/query/query_engine.py
engines/query/query_parser.py
engines/query/query_executor.py
engines/query/query_result_builder.py
```

Internal API:

```python
Query.run("Top Discovery")
Query.run("Company Score", ticker="NVDA")
```

Initial supported queries:

```text
Top Discovery
Top Score
Latest Validation
Latest Proposal
Market Summary
Sector Summary
Company History
Company Score
Company Discovery
Company Validation
```

Search targets:

```text
Companies
Scores
Discovery
Validation
Market
Sectors
Memory
Feedback
Learning
Notifications
```

Query responses use:

```json
{
  "success": true,
  "query": "Top Discovery",
  "data": {},
  "timestamp": "",
  "result_count": 0
}
```

Query history is saved to:

```text
memory/query/history.json
```

Workspace, MCP, Chat Interface, Slack Bot, and Mobile should use Query Engine for search and retrieval instead of each client implementing its own API calls, raw JSON reads, or Markdown parsing.

## Compass MCP Server

Compass Platform 04 adds a thin MCP Server for AI clients.

Files:

```text
mcp/server.py
mcp/tools.py
mcp/resources.py
mcp/prompts.py
mcp/handlers/company_handler.py
mcp/handlers/discovery_handler.py
mcp/handlers/market_handler.py
mcp/handlers/validation_handler.py
```

Run locally over stdio:

```bash
python mcp/server.py
```

Supported AI clients:

```text
ChatGPT
Claude
Codex
```

Future clients:

```text
Cursor
VS Code
Other MCP-compatible AI clients
```

Tools:

```text
company_analysis
top_discovery
market_summary
validation_summary
company_history
```

Resources:

```text
compass://companies
compass://scores
compass://discovery
compass://market
compass://validation
compass://learning
compass://knowledge
```

MCP Server does not contain analysis logic. It routes requests through:

```text
MCP Client
↓
Compass MCP Server
↓
Query Engine
↓
Compass API-facing services
↓
Compass Core
```

This keeps AI clients from reading raw JSON, Markdown, CSV, Memory, or API endpoints directly.

## Time Machine Engine

Compass Lab 01 adds a Historical Replay engine.

Files:

```text
lab/time_machine/time_machine.py
lab/time_machine/snapshot_loader.py
lab/time_machine/timeline_builder.py
lab/time_machine/historical_context.py
```

Run:

```python
from lab.time_machine.time_machine import TimeMachine

TimeMachine.run(date="2024-03-01")
```

Output:

```text
reports/timemachine/snapshot_YYYY-MM-DD.md
reports/timemachine/discovery_YYYY-MM-DD.md
reports/timemachine/market_YYYY-MM-DD.md
```

Time Machine loads only data dated on or before the snapshot date:

```text
Price
Company identity metadata
Financials
News
Events
Knowledge
Memory
```

Time-sensitive company metrics without historical dates are excluded from historical scoring. Knowledge versions created after the snapshot date are excluded. Undated Knowledge markdown is only included when an active Knowledge version exists for the snapshot date.

Difference from Backtesting:

```text
Backtesting
↓
Evaluates what happened after a Discovery signal.

Time Machine
↓
Replays what Compass could have known before future outcomes existed.
```

The purpose is not prediction. It is to reproduce the research environment and inspect what Compass would have surfaced at that point in time.

## Pattern Intelligence Engine

Compass Lab 02 adds Pattern Intelligence.

Files:

```text
lab/pattern_intelligence/pattern_engine.py
lab/pattern_intelligence/pattern_extractor.py
lab/pattern_intelligence/pattern_classifier.py
lab/pattern_intelligence/similarity_engine.py
```

Run:

```python
from lab.pattern_intelligence.pattern_engine import PatternEngine

PatternEngine.run()
```

Inputs:

```text
Discovery History
Validation History
Memory
Learning History
Time Machine results
Financials
Prices
News
Market Intelligence
```

Output:

```text
reports/patterns/success_patterns.md
reports/patterns/failure_patterns.md
reports/patterns/similarity_report.md
reports/patterns/pattern_summary.md
```

Pattern groups:

```text
Success Pattern
Failure Pattern
Sector Pattern
Market Pattern
Event Pattern
Similarity Pattern
```

Pattern Intelligence is connected to Knowledge and Learning, but it does not update either automatically. It creates explainable Knowledge update candidates with evidence and confidence. Human review is required before any pattern becomes Knowledge or influences Learning.

## Theme Intelligence Engine

Compass Lab 03 adds Theme Intelligence.

Files:

```text
lab/theme_intelligence/theme_engine.py
lab/theme_intelligence/theme_classifier.py
lab/theme_intelligence/theme_tracker.py
lab/theme_intelligence/theme_similarity.py
```

Theme definitions:

```text
config/themes.yaml
```

Run:

```python
from lab.theme_intelligence.theme_engine import ThemeEngine

ThemeEngine.run()
```

Inputs:

```text
Companies
Financials
News
Discovery
Validation
Market Intelligence
Pattern Intelligence
Memory
Knowledge
```

Output:

```text
reports/themes/theme_summary.md
reports/themes/theme_ranking.md
reports/themes/theme_similarity.md
reports/themes/{Theme}.md
```

Theme Intelligence organizes Compass research through:

```text
Theme
↓
Market
↓
Sector
↓
Company
```

Companies can belong to multiple themes. For example, one company may be classified into AI, Semiconductor, Cloud, and Robotics when the evidence supports more than one long-term lens.

Relationship with Pattern Intelligence:

```text
Pattern Intelligence
↓
Finds repeated success, failure, sector, market, event, and similarity structures.

Theme Intelligence
↓
Uses those structures as context for long-term theme-level research.
```

Relationship with Discovery:

```text
Discovery
↓
Surfaces company candidates.

Theme Intelligence
↓
Groups candidates into themes and compares theme-level momentum, validation, news, and confidence.
```

Theme Intelligence does not update Knowledge automatically. It creates explainable research views that humans can review before deciding whether a theme should become formal Knowledge.

## Performance Evaluation Engine

Compass Lab 04 adds Performance Evaluation.

Files:

```text
lab/performance/performance_engine.py
lab/performance/evaluator.py
lab/performance/benchmark.py
lab/performance/metrics.py
lab/performance/report_generator.py
```

Run:

```python
from lab.performance.performance_engine import PerformanceEngine

PerformanceEngine.run()
```

Evaluation targets:

```text
Discovery
Discovery Score
Confidence
Theme
Pattern
Market Intelligence
Sector Intelligence
```

Standard periods:

```text
30 days
90 days
180 days
365 days
```

Benchmarks:

```text
S&P500
Nasdaq100
Russell2000
```

Metrics:

```text
Discovery Success Rate
Average Return
Median Return
Win Rate
Loss Rate
Alpha vs Benchmark
Max Drawdown
Average Holding Return
```

Output:

```text
reports/performance/performance_summary.md
reports/performance/discovery_accuracy.md
reports/performance/benchmark_comparison.md
reports/performance/sector_accuracy.md
reports/performance/theme_accuracy.md
reports/performance/dashboard_metrics.json
memory/performance/history.json
```

GitHub Actions:

```text
.github/workflows/performance_evaluation.yml
```

The workflow runs weekly and is independent from the daily pipeline.

Performance Evaluation is not Feedback, Decision, or Learning. It is Compass's scorecard. Future Portfolio integration can use these metrics to compare research signals with realized portfolio outcomes.

## Strategy Evaluation Engine

Compass Lab 05 adds Strategy Evaluation.

Files:

```text
lab/strategy/strategy_engine.py
lab/strategy/strategy_runner.py
lab/strategy/strategy_metrics.py
lab/strategy/portfolio_simulator.py
lab/strategy/allocation_engine.py
```

Configuration:

```text
config/strategy.yaml
```

Initial strategies:

```text
Discovery Score 90+
Discovery Score 85+
High Confidence Only
AI Theme
Semiconductor Theme
Momentum Top
Growth Pattern Match
Composite Strategy
```

Simulation:

```text
Initial capital: 100000 USD
Position sizing: equal weight
Default holding period: 180 days
No real orders
No brokerage connection
```

Risk and portfolio metrics:

```text
CAGR
Total Return
Win Rate
Sharpe Ratio
Max Drawdown
Alpha
Beta
Volatility
Average Holding Period
```

Benchmarks:

```text
S&P500
Nasdaq100
```

Output:

```text
reports/strategy/strategy_summary.md
reports/strategy/portfolio_report.md
reports/strategy/benchmark_report.md
reports/strategy/strategy_ranking.md
reports/strategy/dashboard.json
memory/strategy/strategy_history.json
```

GitHub Actions:

```text
.github/workflows/strategy_evaluation.yml
```

The workflow runs weekly and can also be started manually.

Strategy Evaluation is research-only. It evaluates Compass algorithms and rule sets; it is not investment advice, trade execution, or portfolio management.

## Experiment Engine

Compass Lab 06 adds Experiment Evaluation.

Files:

```text
lab/experiments/experiment_engine.py
lab/experiments/experiment_runner.py
lab/experiments/experiment_registry.py
lab/experiments/comparator.py
lab/experiments/experiment_report.py
```

Configuration:

```text
config/experiments.yaml
```

Experiment fields:

```text
Experiment ID
Name
Description
Target
Baseline Version
Candidate Version
Start Date
End Date
Status
```

Targets:

```text
Discovery Rule
Scoring Rule
Theme Rule
Pattern Rule
Learning Rule
Data Source
```

Comparison metrics:

```text
Discovery Success Rate
Average Return
Alpha
Win Rate
Max Drawdown
Sharpe Ratio
Strategy Ranking
Performance Score
```

Output:

```text
reports/experiments/experiment_summary.md
reports/experiments/experiment_results.md
reports/experiments/experiment_comparison.md
reports/experiments/dashboard.json
memory/experiments/registry.json
```

Winner:

```text
Baseline
Candidate
Tie
Inconclusive
```

GitHub Actions:

```text
.github/workflows/experiment_evaluation.yml
```

Experiments run weekly or manually. They are not part of the daily production workflow.

Experiment Engine is Compass's reproducible A/B testing layer. It records whether a change improved Compass, but it does not promote candidates or modify Knowledge automatically.

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
python collectors/sec/fetch_filings.py --ticker NVDA --limit 1
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
python collectors/earnings/fetch_transcripts.py --ticker NVDA --source-path path/to/transcript.txt --fiscal-quarter "FY2026 Q1"
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
python foundation/data_quality/quality_engine.py
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

## Knowledge Graph Engine

Compass Lab 07 adds a Knowledge Graph Engine for managing relationships between companies, themes, sectors, events, products, technologies, countries, and ETFs.

Files:

```text
lab/knowledge_graph/graph_engine.py
lab/knowledge_graph/graph_builder.py
lab/knowledge_graph/graph_storage.py
lab/knowledge_graph/graph_query.py
lab/knowledge_graph/graph_similarity.py
```

Run locally:

```bash
python lab/knowledge_graph/graph_engine.py
```

Storage:

```text
storage/knowledge_graph/graph.json
storage/knowledge_graph/nodes.json
storage/knowledge_graph/edges.json
```

Reports:

```text
reports/graph/graph_summary.md
reports/graph/company_network.md
reports/graph/theme_network.md
reports/graph/graph.json
```

Node types:

```text
Company
Theme
Sector
Event
Product
Technology
CEO
Country
ETF
```

Relationships:

```text
BELONGS_TO
RELATED_TO
SUPPLIES
COMPETES_WITH
PARTNERS_WITH
USES
INVESTS_IN
ACQUIRES
```

Query API:

```python
Graph.find_related("NVDA")
Graph.find_theme("AI")
Graph.shortest_path("TSMC", "OpenAI")
```

GitHub Actions:

```text
.github/workflows/knowledge_graph.yml
```

The graph is refreshed weekly or manually. It is a Knowledge Layer and does not change scoring, Discovery rules, or Learning automatically.

## Research Notebook

Compass Research 01 adds a Research Notebook for recording the reasoning process behind Compass improvements.

Knowledge is the current accepted rule set. Research Notebook is the historical path that explains how Compass reached those rules.

Files:

```text
research/notebook/notebook_engine.py
research/notebook/notebook_entry.py
research/notebook/experiment_logger.py
research/notebook/hypothesis_tracker.py
```

Notebook entry fields:

```text
Date
Author
Version
Category
Title
Hypothesis
Experiment
Result
Conclusion
Related Knowledge
Related Experiment
```

Standard categories:

```text
Discovery
Theme
Pattern
Data Source
Learning
Strategy
Experiment
Time Machine
Performance
Data Quality
General
```

Storage:

```text
research/entries/YYYY/YYYY-MM-DD/notebook.md
research/entries/YYYY/YYYY-MM-DD/metadata.json
research/notebook_index.json
```

Search API:

```python
Notebook.search("ETF")
Notebook.search(category="Experiment")
```

Reports and Workspace data:

```text
reports/research/monthly_summary.md
reports/research/yearly_summary.md
reports/research/hypothesis_status.md
reports/research/notebook_dashboard.json
```

Notebook generation is not automated by GitHub Actions. It is written by humans or by explicit tools such as `ExperimentLogger` after review.

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
