from typing import Any

from engines.query.query_engine import Query


def validation_summary(arguments: dict[str, Any]) -> dict[str, Any]:
    ticker = arguments.get("ticker")
    if ticker:
        return Query.run("Company Validation", ticker=str(ticker).upper())
    return Query.run("Latest Validation", limit=int(arguments.get("limit", 20)))
