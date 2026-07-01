import re
from typing import Any

from engines.query.query_engine import Query


def extract_ticker(value: str | None, fallback: str = "NVDA") -> str:
    if not value:
        return fallback
    match = re.search(r"\b[A-Z]{1,5}\b", value.upper())
    return match.group(0) if match else fallback


def company_analysis(arguments: dict[str, Any]) -> dict[str, Any]:
    ticker = extract_ticker(arguments.get("ticker") or arguments.get("request"))
    return {
        "ticker": ticker,
        "company": Query.run("Company History", ticker=ticker),
        "score": Query.run("Company Score", ticker=ticker),
        "discovery": Query.run("Company Discovery", ticker=ticker),
        "validation": Query.run("Company Validation", ticker=ticker),
    }


def company_history(arguments: dict[str, Any]) -> dict[str, Any]:
    ticker = extract_ticker(arguments.get("ticker") or arguments.get("request"))
    return Query.run("Company History", ticker=ticker)
