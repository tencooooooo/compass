from __future__ import annotations

import csv
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT


class PortfolioSimulator:
    """Runs simple equal-weight virtual portfolio simulations."""

    def __init__(self, repo_root: Path = REPO_ROOT, initial_capital: float = 100000.0, holding_days: int = 180) -> None:
        self.repo_root = repo_root
        self.initial_capital = initial_capital
        self.holding_days = holding_days

    def simulate(self, name: str, holdings: list[dict[str, Any]], signal_date: date) -> dict[str, Any]:
        if not holdings:
            return {
                "strategy": name,
                "initial_capital": self.initial_capital,
                "ending_value": self.initial_capital,
                "total_return": 0.0,
                "holdings": [],
                "trades": [],
                "equity_curve": [{"date": signal_date.isoformat(), "value": self.initial_capital}],
                "status": "no_positions",
            }
        trades = []
        ending_value = 0.0
        for holding in holdings:
            ticker = holding["ticker"]
            weight = float(holding["weight"])
            prices = self._prices(ticker)
            entry = self._price_on_or_before(prices, signal_date)
            target_exit_date = signal_date + timedelta(days=self.holding_days)
            exit_row = self._price_on_or_before(prices, target_exit_date)
            if not entry or not exit_row:
                continue
            allocated = self.initial_capital * weight
            shares = allocated / float(entry["close"]) if float(entry["close"]) else 0
            exit_value = shares * float(exit_row["close"])
            ending_value += exit_value
            trades.append(
                {
                    "ticker": ticker,
                    "weight": weight,
                    "entry_date": entry["date"],
                    "entry_price": float(entry["close"]),
                    "exit_date": exit_row["date"],
                    "target_exit_date": target_exit_date.isoformat(),
                    "exit_price": float(exit_row["close"]),
                    "shares": round(shares, 6),
                    "allocated": round(allocated, 2),
                    "ending_value": round(exit_value, 2),
                    "return_percent": round((exit_value - allocated) / allocated * 100, 2) if allocated else None,
                    "holding_days": (date.fromisoformat(exit_row["date"]) - date.fromisoformat(entry["date"])).days,
                    "matured": date.fromisoformat(exit_row["date"]) >= target_exit_date,
                }
            )
        cash = self.initial_capital * (1 - sum(float(row["weight"]) for row in holdings if row.get("ticker") in {trade["ticker"] for trade in trades}))
        ending_value += cash
        return {
            "strategy": name,
            "initial_capital": self.initial_capital,
            "ending_value": round(ending_value, 2),
            "total_return": round((ending_value - self.initial_capital) / self.initial_capital * 100, 2),
            "holdings": holdings,
            "trades": trades,
            "equity_curve": self._equity_curve(signal_date, trades, cash),
            "status": self._status(trades),
        }

    def _equity_curve(self, signal_date: date, trades: list[dict[str, Any]], cash: float) -> list[dict[str, Any]]:
        if not trades:
            return [{"date": signal_date.isoformat(), "value": self.initial_capital}]
        start_value = self.initial_capital
        end_date = max(trade["exit_date"] for trade in trades)
        end_value = sum(trade["ending_value"] for trade in trades) + cash
        return [
            {"date": signal_date.isoformat(), "value": round(start_value, 2)},
            {"date": end_date, "value": round(end_value, 2)},
        ]

    def _prices(self, ticker: str) -> list[dict[str, Any]]:
        path = self.repo_root / "storage" / "raw" / "prices" / f"{ticker}.csv"
        if not path.exists():
            return []
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))

    def _price_on_or_before(self, prices: list[dict[str, Any]], target: date) -> dict[str, Any] | None:
        for row in reversed(prices):
            try:
                row_date = date.fromisoformat(row["date"])
            except (KeyError, ValueError):
                continue
            if row_date <= target:
                return row
        return None

    def _status(self, trades: list[dict[str, Any]]) -> str:
        if not trades:
            return "no_price_data"
        if all(trade.get("matured") for trade in trades):
            return "completed"
        return "partial_period"
