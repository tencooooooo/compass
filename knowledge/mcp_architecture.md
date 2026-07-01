# MCP Architecture

Compass MCP Server is the AI client connection layer for Compass.

## Purpose

- Allow ChatGPT, Claude, Codex, and future MCP clients to query Compass.
- Keep analysis logic inside Compass.
- Route all tool calls through Query Engine.
- Avoid direct API or file access from MCP tools.

## Flow

```text
MCP Client
↓
Compass MCP Server
↓
Query Engine
↓
Compass API-facing services
↓
Compass Core data, reports, memory, and knowledge
```

## Rule

MCP Server is a thin interface. It does not analyze, score, validate, or learn.
