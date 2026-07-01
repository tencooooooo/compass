# API Design

Compass API is the read-only data interface for Compass.

## Purpose

- Provide one stable interface for generated Compass data.
- Keep Workspace, Mobile, Slack Bot, MCP, and external AI integrations away from raw file paths.
- Preserve the current artifact-based pipeline while preparing for API-backed storage.

## Current Scope

- Read only
- JSON responses
- OpenAPI and Swagger UI enabled
- No authentication required yet

## Response Contract

All API responses should use:

```json
{
  "success": true,
  "data": {},
  "timestamp": "",
  "version": "v1"
}
```

Errors should use the same envelope with `success: false` and an `error` object.

## Design Principle

Routes should not know file layout details. File access belongs in the service layer so future S3, database, or API storage can replace local artifacts without changing route behavior.
