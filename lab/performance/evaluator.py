from __future__ import annotations

import csv
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT, list_json_files, read_json
from lab.performance.benchmark import Benchmark
from utils.price_data import adjusted_close


DEFAULT_PERIODS = (30, 90, 180, 365)


class Evaluator:
    """Evaluates past Compass signals against later price movement."""

    def __init__(self, repo_root: Path = REPO_ROOT, periods: tuple[int, ...] = DEFAULT_PERIODS) -> None:
        self.repo_root = repo_root
        self.periods = periods
        self.benchmark = Benchmark(repo_root=repo_root)

    def evaluate(self) -> dict[str, Any]:
        signals = self._signals()
        rows = []
        for signal in signals:
            for period in self.periods:
                rows.append(self._evaluate_signal(signal, period))
        return {
            "evaluation_date": date.today().isoformat(),
            "periods": list(self.periods),
            "signals": signals,
            "rows": rows,
        }

    def _signals(self) -> list[dict[str, Any]]:
        latest = read_json("reports/discovery/discovery_candidates.json", {})
        candidates = latest.get("candidates", []) if isinstance(latest, dict) else []
        generated_at = latest.get("generated_at") if isinstance(latest, dict) else None
        discovery_date = self._date_from_datetime(generated_at) or date.today()
        theme_map = self._themes_by_ticker()
        pattern_map = self._patterns_by_ticker()
        signals = []
        for candidate in candidates:
            ticker = str(candidate.get("ticker", "")).upper()
            if not ticker:
                continue
            signals.append(
                {
                    "ticker": ticker,
                    "company": candidate.get("company") or ticker,
                    "sector": candidate.get("sector") or "Unknown",
                    "industry": candidate.get("industry") or "Unknown",
                    "discovery_date": discovery_date.isoformat(),
                    "discovery_score": candidate.get("discovery_score"),
                    "discovery_score_bucket": self._score_bucket(candidate.get("discovery_score")),
                    "confidence": candidate.get("confidence") or "Unknown",
                    "themes": theme_map.get(ticker, []),
                    "patterns": pattern_map.get(ticker, []),
                    "market_status": self._market_status(latest.get("market", {})),
                    "market_intelligence": latest.get("market", {}),
                    "sector_intelligence": {
                        "sector_average_score": candidate.get("metrics", {}).get("sector_average_score"),
                    },
                }
            )
        return signals

    def _evaluate_signal(self, signal: dict[str, Any], period: int) -> dict[str, Any]:
        start_date = date.fromisoformat(signal["discovery_date"])
        target_date = start_date + timedelta(days=period)
        prices = self._prices(signal["ticker"])
        start = self._price_on_or_after(prices, start_date)
        end = self._price_on_or_before(prices, target_date)
        benchmark = self.benchmark.compare(start_date, target_date)
        benchmark_return = benchmark.get("average_return_percent")
        row = {
            **signal,
            "period": period,
            "target_date": target_date.isoformat(),
            "benchmark": benchmark,
            "benchmark_return_percent": benchmark_return,
        }
        if not start or not end or date.fromisoformat(end["date"]) < target_date:
            row.update(
                {
                    "status": "pending",
                    "start_price": adjusted_close(start) if start else None,
                    "end_price": adjusted_close(end) if end else None,
                    "return_percent": None,
                    "alpha_percent": None,
                }
            )
            return row
        start_price = adjusted_close(start)
        end_price = adjusted_close(end)
        if start_price is None or end_price is None:
            row.update(
                {
                    "status": "missing_price",
                    "start_price": start_price,
                    "end_price": end_price,
                    "return_percent": None,
                    "alpha_percent": None,
                }
            )
            return row
        return_percent = round((end_price - start_price) / start_price * 100, 2) if start_price else None
        alpha = round(return_percent - benchmark_return, 2) if return_percent is not None and benchmark_return is not None else None
        row.update(
            {
                "status": "completed",
                "start_price": start_price,
                "end_price": end_price,
                "actual_start_date": start["date"],
                "actual_end_date": end["date"],
                "return_percent": return_percent,
                "alpha_percent": alpha,
            }
        )
        return row

    def _prices(self, ticker: str) -> list[dict[str, Any]]:
        path = self.repo_root / "storage" / "raw" / "prices" / f"{ticker}.csv"
        if not path.exists():
            return []
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))

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

    def _date_from_datetime(self, value: str | None) -> date | None:
        if not value:
            return None
        try:
            return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
        except ValueError:
            return None

    def _themes_by_ticker(self) -> dict[str, list[str]]:
        output: dict[str, list[str]] = {}
        theme_root = self.repo_root / "reports" / "themes"
        if not theme_root.exists():
            return output
        for path in theme_root.glob("*.md"):
            if path.name.startswith("theme_"):
                continue
            theme = path.stem.replace("_", " ")
            text = path.read_text(encoding="utf-8", errors="ignore")
            for ticker in self._known_tickers():
                if f"- {ticker} " in text or f"- {ticker} -" in text:
                    output.setdefault(ticker, []).append(theme)
        return output

    def _patterns_by_ticker(self) -> dict[str, list[str]]:
        output: dict[str, list[str]] = {}
        pattern_root = self.repo_root / "reports" / "patterns"
        if not pattern_root.exists():
            return output
        for path in pattern_root.glob("*patterns.md"):
            label = path.stem.replace("_", " ")
            text = path.read_text(encoding="utf-8", errors="ignore")
            for ticker in self._known_tickers():
                if ticker in text:
                    output.setdefault(ticker, []).append(label)
        return output

    def _known_tickers(self) -> set[str]:
        tickers = {path.stem.upper() for path in list_json_files("storage/raw/companies")}
        price_root = self.repo_root / "storage" / "raw" / "prices"
        if price_root.exists():
            tickers.update(path.stem.upper() for path in price_root.glob("*.csv"))
        return tickers

    def _score_bucket(self, score: Any) -> str:
        try:
            value = float(score)
        except (TypeError, ValueError):
            return "Unknown"
        if value >= 80:
            return "80+"
        if value >= 70:
            return "70-79"
        if value >= 60:
            return "60-69"
        return "Below 60"

    def _market_status(self, market: dict[str, Any]) -> str:
        if not isinstance(market, dict):
            return "Unknown"
        momentum = market.get("average_momentum_1m")
        try:
            value = float(momentum)
        except (TypeError, ValueError):
            return "Unknown"
        if value > 5:
            return "Risk-On"
        if value < -5:
            return "Risk-Off"
        return "Neutral"
