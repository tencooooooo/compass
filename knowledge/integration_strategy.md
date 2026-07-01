# Integration Strategy

Compass API is the single public data interface for future clients.

## Target Clients

- Workspace
- Mobile
- Slack Bot
- MCP
- External AI
- Internal automation

## Current Integration

The API reads local generated artifacts from:

```text
reports/
storage/
memory/
```

## Future Integration

```text
Local artifacts
↓
Compass API
↓
Workspace / Mobile / Slack / MCP / External AI
```

Storage can later move to S3, Postgres, Supabase, or another database without requiring clients to read raw Compass files.

## Authentication Plan

Authentication is not required for the first local read-only API. Future options:

- API Key
- JWT
- OAuth

Authentication must be added without changing the response envelope.
