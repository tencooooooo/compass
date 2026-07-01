# Provider Design

Compass providers adapt normalized agent context to model-specific clients.

## Current Provider

```text
DummyProvider
```

DummyProvider performs no model inference. It returns the prompt preview and context so local development remains deterministic.

## Future Providers

```text
OpenAIProvider
ClaudeProvider
GeminiProvider
MCPProvider
```

## Provider Rules

- Providers must not mutate Knowledge, Memory, or reports.
- Providers receive prepared context from agents.
- Providers return structured responses.
- Provider-specific authentication must stay outside agent logic.
- Failed provider calls should not corrupt Compass data.

## Design Goal

AI models should be replaceable. Compass remains the research platform and source of truth.

## Data Source Providers

Data Source Hub uses a separate provider concept for external and local data sources.

Initial Data Source providers:

```text
YahooFinanceProvider
SECProvider
FREDProvider
FinnhubProvider
AlphaVantageProvider
CSVProvider
PDFProvider
JSONProvider
```

Every Data Source provider implements:

```python
connect()
fetch()
normalize()
validate()
cache()
disconnect()
```

Provider rules:

- Compass Core should not know whether data came from API, CSV, PDF, JSON, or a future database.
- API keys must be read from environment variables or GitHub Secrets.
- Provider-specific schemas must be normalized before use by engines.
- Cache behavior must stay inside the provider layer.
- Disabled providers must fail gracefully without breaking existing workflows.
