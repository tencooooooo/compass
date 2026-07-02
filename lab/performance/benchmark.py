from __future__ import annotations

import csv
from datetime import date
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT
from utils.price_data import adjusted_close


DEFAULT_BENCHMARKS = {
    "S&P500": "SPY",
    "Nasdaq100": "QQQ",
    "Russell2000": "IWM",
}


class Benchmark:
    """Calculates benchmark returns when benchmark price files are available."""

    def __init__(self, repo_root: Path = REPO_ROOT, benchmarks: dict[str, str] | None = None) -> None:
        self.repo_root = repo_root
        self.benchmarks = benchmarks or DEFAULT_BENCHMARKS

    def compare(self, start_date: date, end_date: date) -> dict[str, Any]:
        output = {}
        for name, ticker in self.benchmarks.items():
            prices = self._prices(ticker)
            result = self._return(prices, start_date, end_date)
            output[name] = {"ticker": ticker, **result}
        available = [item["return_percent"] for item in output.values() if isinstance(item.get("return_percent"), (int, float))]
        average = round(sum(available) / len(available), 2) if available else None
        return {"benchmarks": output, "average_return_percent": average}

    def _prices(self, ticker: str) -> list[dict[str, Any]]:
        path = self.repo_root / "storage" / "raw" / "prices" / f"{ticker}.csv"
        if not path.exists():
            return []
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))

    def _return(self, prices: list[dict[str, Any]], start_date: date, end_date: date) -> dict[str, Any]:
        start = self._price_on_or_after(prices, start_date)
        end = self._price_on_or_before(prices, end_date)
        if not start or not end:
            return {"status": "missing_data", "return_percent": None}
        start_price = adjusted_close(start)
        end_price = adjusted_close(end)
        if start_price in (None, 0) or end_price is None:
            return {"status": "invalid_start_price", "return_percent": None}
        return {
            "status": "completed",
            "start_date": start["date"],
            "end_date": end["date"],
            "return_percent": round((end_price - start_price) / start_price * 100, 2),
        }

    def _price_on_or_after(self, prices: list[dict[str, Any]], target: date) -> dict[str, Any] | None:
        for row in prices:
            if date.fromisoformat(row["date"]) >= target:
                return row
        return None

    def _price_on_or_before(self, prices: list[dict[str, Any]], target: date) -> dict[str, Any] | None:
        for row in reversed(prices):
            if date.fromisoformat(row["date"]) <= target:
                return row
        return None
