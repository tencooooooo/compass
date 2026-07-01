# Data Source Architecture

Data Source Hub is the provider layer for Compass data access.

It sits below collectors and analysis engines:

```text
Compass Core
↓
Collectors and Engines
↓
Data Source Hub
↓
Provider
↓
API, CSV, PDF, JSON, or future Database
```

Goals:

- Keep Compass Core independent from data-source details.
- Add new providers without changing analyzers or engines.
- Normalize source-specific responses before they reach Compass.
- Keep API keys outside code.
- Prepare for cache and database-backed storage without forcing that migration now.

Every provider implements:

```python
connect()
fetch()
normalize()
validate()
cache()
disconnect()
```

Current implementation is intentionally conservative. API-key providers are scaffolds only.
