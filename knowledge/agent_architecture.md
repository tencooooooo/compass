# Agent Architecture

Compass Agent Layer is a model-independent orchestration layer.

## Purpose

- Prepare Compass context for AI systems.
- Keep Compass analysis logic independent from ChatGPT, Codex, Claude, Gemini, MCP, or any other client.
- Use Compass API-facing services as the source of truth.
- Avoid direct Knowledge, Memory, or report updates from agents.

## Layers

```text
Compass Data
↓
Compass API
↓
Context Builder
↓
Agent
↓
Provider
↓
AI Client
```

## Agents

- Base Agent: common lifecycle and interface.
- Research Agent: company analysis, comparison, and report context.
- Discovery Agent: candidates, reasons, evidence, and confidence.
- Market Agent: market intelligence and sector context.
- Portfolio Agent: future placeholder only.

## Rule

Agents organize and explain context. They do not own investment decisions and do not mutate Knowledge automatically.
