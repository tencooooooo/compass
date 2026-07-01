# Query Architecture

Query Engine is the internal search layer for Compass.

## Flow

```text
Client
↓
Query.run()
↓
Query Parser
↓
Query Executor
↓
API-facing services / Memory / Reports
↓
Query Result Builder
↓
Query History
```

## Components

- `query_engine.py`: public internal API.
- `query_parser.py`: maps named queries to normalized intents.
- `query_executor.py`: retrieves data across Compass sources.
- `query_result_builder.py`: builds the unified response envelope.

## Response Shape

```json
{
  "success": true,
  "query": "Top Discovery",
  "data": {},
  "timestamp": "",
  "result_count": 0
}
```

## History

Query history is stored in:

```text
memory/query/history.json
```

History records query, timestamp, result count, and success status.
