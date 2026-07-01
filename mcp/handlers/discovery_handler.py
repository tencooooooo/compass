from typing import Any

from engines.query.query_engine import Query


def top_discovery(arguments: dict[str, Any]) -> dict[str, Any]:
    limit = int(arguments.get("limit", 5))
    return Query.run("Top Discovery", limit=limit)
