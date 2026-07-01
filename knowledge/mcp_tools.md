# MCP Tools

Compass MCP Server exposes tools that call Query Engine.

## Tools

```text
company_analysis
top_discovery
market_summary
validation_summary
company_history
```

## Tool Responsibilities

- `company_analysis`: company report, latest score, discovery, and validation.
- `top_discovery`: top Discovery candidates.
- `market_summary`: Market Intelligence summary.
- `validation_summary`: latest Validation results.
- `company_history`: Memory, history, learning, and feedback context.

## Constraints

- Tools are read-only.
- Tools do not mutate Knowledge, Memory, scoring, or reports.
- Tools must call Query Engine rather than Compass API directly.
