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
