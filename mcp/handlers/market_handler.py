from typing import Any

from engines.query.query_engine import Query


def market_summary(arguments: dict[str, Any]) -> dict[str, Any]:
    return Query.run("Market Summary")
