import json
from typing import Any, Callable

from mcp.handlers.company_handler import company_analysis, company_history
from mcp.handlers.discovery_handler import top_discovery
from mcp.handlers.market_handler import market_summary
from mcp.handlers.validation_handler import validation_summary


ToolHandler = Callable[[dict[str, Any]], dict[str, Any]]


TOOLS: dict[str, dict[str, Any]] = {
    "company_analysis": {
        "description": "Return company report, latest score, discovery, and validation context.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "ticker": {"type": "string", "description": "Ticker symbol such as NVDA."},
                "request": {"type": "string", "description": "Natural-language request such as Analyze NVDA."},
            },
        },
        "handler": company_analysis,
    },
    "top_discovery": {
        "description": "Return top Discovery candidates from Compass Query Engine.",
        "inputSchema": {
            "type": "object",
            "properties": {"limit": {"type": "integer", "default": 5, "minimum": 1, "maximum": 20}},
        },
        "handler": top_discovery,
    },
    "market_summary": {
        "description": "Return Market Intelligence summary.",
        "inputSchema": {"type": "object", "properties": {}},
        "handler": market_summary,
    },
    "validation_summary": {
        "description": "Return latest Validation results, optionally for one ticker.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "ticker": {"type": "string"},
                "limit": {"type": "integer", "default": 20, "minimum": 1, "maximum": 100},
            },
        },
        "handler": validation_summary,
    },
    "company_history": {
        "description": "Return Memory, history, learning, and feedback context for a company.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "ticker": {"type": "string"},
                "request": {"type": "string", "description": "Natural-language request such as Show NVDA History."},
            },
        },
        "handler": company_history,
    },
}


def list_tools() -> list[dict[str, Any]]:
    return [
        {
            "name": name,
            "description": definition["description"],
            "inputSchema": definition["inputSchema"],
        }
        for name, definition in TOOLS.items()
    ]


def call_tool(name: str, arguments: dict[str, Any] | None = None) -> list[dict[str, str]]:
    definition = TOOLS.get(name)
    if definition is None:
        raise ValueError(f"Unknown MCP tool: {name}")
    result = definition["handler"](arguments or {})
    return [{"type": "text", "text": json.dumps(result, indent=2, ensure_ascii=False)}]
