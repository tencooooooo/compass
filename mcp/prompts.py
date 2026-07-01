from typing import Any

from api.services.data_loader import read_text


PROMPTS: dict[str, dict[str, Any]] = {
    "compass_mcp": {
        "description": "General prompt for AI clients using Compass MCP Server.",
        "arguments": [],
        "file": "prompts/mcp_prompt.md",
    },
    "company_analysis": {
        "description": "Prompt for company analysis through Compass Query Engine.",
        "arguments": [{"name": "ticker", "description": "Ticker symbol", "required": True}],
        "file": "prompts/company_analysis_prompt.md",
    },
    "discovery": {
        "description": "Prompt for Discovery candidate review.",
        "arguments": [],
        "file": "prompts/query_prompt.md",
    },
    "market": {
        "description": "Prompt for Market Intelligence review.",
        "arguments": [],
        "file": "prompts/market_intelligence_prompt.md",
    },
    "validation": {
        "description": "Prompt for Validation review.",
        "arguments": [],
        "file": "prompts/validation_prompt.md",
    },
}


def list_prompts() -> list[dict[str, Any]]:
    return [
        {
            "name": name,
            "description": definition["description"],
            "arguments": definition["arguments"],
        }
        for name, definition in PROMPTS.items()
    ]


def get_prompt(name: str, arguments: dict[str, Any] | None = None) -> dict[str, Any]:
    definition = PROMPTS.get(name)
    if definition is None:
        raise ValueError(f"Unknown MCP prompt: {name}")
    text = read_text(definition["file"], "Use Compass Query Engine and do not invent missing data.")
    if arguments:
        for key, value in arguments.items():
            text = text.replace(f"{{{{{key}}}}}", str(value))
    return {
        "description": definition["description"],
        "messages": [
            {
                "role": "user",
                "content": {"type": "text", "text": text},
            }
        ],
    }
