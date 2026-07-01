# Collector Guidelines

All new Compass collectors should follow the same interface:

```python
collect()
validate()
normalize()
save()
```

Guidelines:

- Keep source-specific logic inside the collector.
- Do not let analysis engines call external data providers directly.
- Save raw or normalized outputs under `storage/raw/{category}/`.
- Validate required fields before saving.
- Normalize timestamps, identifiers, tickers, and numeric values.
- Record the source name and collection timestamp.
- Treat API keys and credentials as runtime configuration only.
- Keep collectors disabled until the source, cost, license, and rate limits are reviewed.

Collectors should be boring and reliable. Analysis quality should improve because the data is better, not because collection logic becomes clever.
