import json
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT
from engines.query.query_engine import Query


RESOURCE_QUERIES = {
    "compass://companies": ("Companies", {}),
    "compass://scores": ("Scores", {}),
    "compass://discovery": ("Discovery", {}),
    "compass://market": ("Market", {}),
    "compass://validation": ("Validation", {}),
    "compass://learning": ("Learning", {}),
}


def list_resources() -> list[dict[str, Any]]:
    resources = [
        {
            "uri": uri,
            "name": uri.replace("compass://", "").title(),
            "description": f"Compass {uri.replace('compass://', '')} resource",
            "mimeType": "application/json",
        }
        for uri in RESOURCE_QUERIES
    ]
    resources.append(
        {
            "uri": "compass://knowledge",
            "name": "Knowledge",
            "description": "Human-maintained Compass Knowledge markdown files",
            "mimeType": "application/json",
        }
    )
    return resources


def read_resource(uri: str) -> list[dict[str, str]]:
    if uri == "compass://knowledge":
        payload = _read_knowledge()
    elif uri in RESOURCE_QUERIES:
        query, params = RESOURCE_QUERIES[uri]
        payload = Query.run(query, **params)
    else:
        raise ValueError(f"Unknown MCP resource: {uri}")
    return [{"uri": uri, "mimeType": "application/json", "text": json.dumps(payload, indent=2, ensure_ascii=False)}]


def _read_knowledge() -> dict[str, str]:
    knowledge_root = REPO_ROOT / "knowledge"
    items: dict[str, str] = {}
    if not knowledge_root.exists():
        return items
    for path in sorted(knowledge_root.glob("*.md")):
        items[path.name] = path.read_text(encoding="utf-8")
    return items
