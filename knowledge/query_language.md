# Query Language

Compass Query Language starts as a controlled set of named queries.

## Initial Queries

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

## Internal API

```python
Query.run("Top Discovery")
Query.run("Company Score", ticker="NVDA")
```

## Parameters

- `ticker`: company ticker for company-specific queries.
- `limit`: maximum number of rows for ranked or latest queries.

## Principle

Clients should not implement their own file search, API stitching, or raw report parsing. Workspace, Chat Interface, MCP, Slack Bot, and Mobile should call Query Engine so the same query returns the same meaning everywhere.
