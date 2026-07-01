# Context Design

Compass context must be stable across AI providers.

## Sources

- API data
- Knowledge
- Memory
- Reports

## Context Shape

Context should be structured dictionaries with explicit keys such as:

```text
company
score
discovery
validation
market
sectors
proposals
learning
knowledge
reports
```

## Principles

- Keep source evidence visible.
- Preserve confidence and uncertainty.
- Avoid provider-specific prompt formats in context.
- Prefer API-facing services over direct ad hoc file reads.
- Include only relevant context for each agent.

## Future Direction

The same context objects should support:

- Workspace
- MCP tools
- ChatGPT
- Codex
- Claude
- Gemini
- Slack Bot
