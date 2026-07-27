# Platform Layer

Workspace・API・Agent・Query・MCP という、Compassの外部インターフェース層です。

[← README に戻る](../../README.md)

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
python -m mcp.server
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
