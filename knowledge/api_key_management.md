# API Key Management

Compass must never store API keys in source code.

Allowed sources:

- GitHub Secrets
- Local `.env`
- Runtime environment variables

Provider configuration may define the environment variable name:

```yaml
datasources:
  fred:
    enabled: false
    api_key_env: FRED_API_KEY
```

Rules:

- API keys are read at runtime only.
- Missing keys should disable or fail provider access cleanly.
- Logs must not print secret values.
- Test fixtures must not include real credentials.
- Providers should document required scopes, rate limits, and expected costs before activation.

Current state:

- Yahoo Finance, CSV, and JSON do not require API keys.
- FRED, Finnhub, and Alpha Vantage are scaffolded with environment variable names only.
- No API-key-backed provider performs a real external connection yet.
