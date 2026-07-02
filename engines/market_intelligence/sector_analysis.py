from __future__ import annotations

from collections import defaultdict
from typing import Any

import pandas as pd

from utils.price_data import trading_day_momentum
from utils.values import safe_float


def average(values: list[Any]) -> float | None:
    numbers = [safe_float(value) for value in values]
    numbers = [value for value in numbers if value is not None]
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def momentum_for_days(prices: pd.DataFrame, days: int) -> float | None:
    return trading_day_momentum(prices, days)


def calculate_ticker_momentum(prices: pd.DataFrame) -> dict[str, float | None]:
    if prices.empty:
        return {"1m": None, "3m": None, "6m": None, "1y": None}
    return {
        "1m": momentum_for_days(prices, 30),
        "3m": momentum_for_days(prices, 90),
        "6m": momentum_for_days(prices, 180),
        "1y": momentum_for_days(prices, 365),
    }


def momentum_label(value: float | None) -> str:
    if value is None:
        return "Unknown"
    if value >= 10:
        return "Strong"
    if value >= 0:
        return "Positive"
    if value >= -10:
        return "Weak"
    return "Risk-Off"


def news_label(news_count: int) -> str:
    if news_count >= 15:
        return "High"
    if news_count >= 5:
        return "Medium"
    return "Low"


def financial_health_label(score: float | None) -> str:
    if score is None:
        return "Unknown"
    if score >= 15:
        return "Good"
    if score >= 10:
        return "Neutral"
    return "Watch"


def build_sector_summaries(ticker_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in ticker_rows:
        sector = row.get("sector") or "Unknown"
        grouped[sector].append(row)

    summaries: list[dict[str, Any]] = []
    for sector, rows in sorted(grouped.items()):
        avg_score = average([row.get("total_score") for row in rows])
        avg_per = average([row.get("trailing_pe") for row in rows])
        avg_eps = average([row.get("eps") for row in rows])
        avg_momentum = average([row.get("momentum_1m") for row in rows])
        avg_financial_health = average([row.get("financial_health_score") for row in rows])
        news_count = sum(int(row.get("news_count") or 0) for row in rows)

        summaries.append(
            {
                "sector": sector,
                "ticker_count": len(rows),
                "tickers": [row["ticker"] for row in rows],
                "average_score": avg_score,
                "average_per": avg_per,
                "average_eps": avg_eps,
                "average_momentum_1m": avg_momentum,
                "news_count": news_count,
                "trend": {
                    "momentum": momentum_label(avg_momentum),
                    "news": news_label(news_count),
                    "financial_health": financial_health_label(avg_financial_health),
                },
            }
        )
    return summaries
