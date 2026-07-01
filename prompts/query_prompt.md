# Compass Query Prompt

Use Query Engine for all Compass search and retrieval.

Rules:

- Do not read raw Compass files directly from client code when a Query exists.
- Prefer `Query.run(...)` as the internal search interface.
- Preserve the unified query result shape.
- Include query name, timestamp, success state, and result count.
- Keep query behavior stable for Workspace, Chat Interface, MCP, Slack Bot, and Mobile.
- If a query is unsupported, return a clear failure result instead of guessing.
