# Compass API Prompt

Use this prompt when extending Compass API behavior.

Compass API is a read-only interface for Compass research data. It must preserve stable response contracts, explicit versioning, and human-readable error behavior.

Rules:

- Do not add write endpoints unless explicitly approved.
- Keep routes under `/api/v1/` until a reviewed version change is required.
- Return JSON through the unified response envelope.
- Keep raw file access inside service modules.
- Preserve Swagger/OpenAPI compatibility.
- Design for Workspace, Mobile, Slack Bot, MCP, and external AI clients.
- Do not expose secrets, environment variables, or local machine paths.
