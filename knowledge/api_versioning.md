# API Versioning

Compass API starts at:

```text
/api/v1/
```

## Compatibility Policy

- Keep existing v1 fields backward compatible whenever possible.
- Add fields instead of renaming or removing fields.
- Introduce `/api/v2/` when response meaning or structure must change.
- Keep old versions available long enough for Workspace, Mobile, Slack, MCP, and external AI clients to migrate.

## Version Ownership

API version changes require human review because downstream tools may depend on stable response contracts.

## Future Direction

```text
/api/v1/
↓
/api/v2/
↓
/api/v3/
```

Each version should have explicit migration notes and tests.
