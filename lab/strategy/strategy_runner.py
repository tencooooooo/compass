from __future__ import annotations

from datetime import date, datetime
import csv
from pathlib import Path
from typing import Any

import yaml

from api.services.data_loader import REPO_ROOT, read_json
from lab.strategy.allocation_engine import AllocationEngine
from lab.strategy.portfolio_simulator import PortfolioSimulator
from lab.strategy.strategy_metrics import StrategyMetrics
from utils.price_data import adjusted_close


class StrategyRunner:
    """Builds strategies from Compass signals and runs virtual simulations."""

    def __init__(self, repo_root: Path = REPO_ROOT) -> None:
        self.repo_root = repo_root
        self.config = yaml.safe_load((repo_root / "config" / "strategy.yaml").read_text(encoding="utf-8"))
        self.allocator = AllocationEngine()
        self.metrics = StrategyMetrics()
        self.simulator = PortfolioSimulator(
            repo_root=repo_root,
            initial_capital=float(self.config.get("initial_capital", 100000)),
            holding_days=int(self.config.get("sell", {}).get("holding_days", 180)),
        )

    def run(self) -> dict[str, Any]:
        candidates = self._candidates()
        signal_date = self._signal_date()
        strategies = self.config.get("strategies", {})
        results = []
        for key, strategy in strategies.items():
            selected = self.allocator.select(strategy, candidates)
            simulation = self.simulator.simulate(key, selected, signal_date)
            benchmark_return = self._benchmark_return(signal_date)
            metrics = self.metrics.calculate(simulation, benchmark_return=benchmark_return)
            results.append(
                {
                    "strategy_id": key,
                    "label": strategy.get("label", key),
                    "rules": strategy,
                    "selected_count": len(selected),
                    "simulation": simulation,
                    "metrics": metrics,
                    "benchmark_return": benchmark_return,
                }
            )
        return {
            "evaluation_date": date.today().isoformat(),
            "signal_date": signal_date.isoformat(),
            "initial_capital": self.config.get("initial_capital", 100000),
            "results": results,
        }

    def _candidates(self) -> list[dict[str, Any]]:
        discovery = read_json("reports/discovery/discovery_candidates.json", {})
        rows = discovery.get("candidates", []) if isinstance(discovery, dict) else []
        themes = self._themes_by_ticker()
        patterns = self._patterns_by_ticker()
        output = []
        for row in rows:
            ticker = str(row.get("ticker", "")).upper()
            if not ticker:
                continue
            momentum = row.get("metrics", {}).get("momentum", {})
            output.append(
                {
                    "ticker": ticker,
                    "company": row.get("company") or ticker,
                    "sector": row.get("sector") or "Unknown",
                    "industry": row.get("industry") or "Unknown",
                    "discovery_score": row.get("discovery_score"),
                    "confidence": row.get("confidence") or "Unknown",
                    "themes": themes.get(ticker, []),
                    "patterns": patterns.get(ticker, []),
                    "momentum_3m": momentum.get("3m"),
                }
            )
        return output

    def _signal_date(self) -> date:
        discovery = read_json("reports/discovery/discovery_candidates.json", {})
        generated_at = discovery.get("generated_at") if isinstance(discovery, dict) else None
        if generated_at:
            try:
                return datetime.fromisoformat(generated_at.replace("Z", "+00:00")).date()
            except ValueError:
                pass
        return date.today()

    def _themes_by_ticker(self) -> dict[str, list[str]]:
        output: dict[str, list[str]] = {}
        root = self.repo_root / "reports" / "themes"
        if not root.exists():
            return output
        tickers = self._known_tickers()
        for path in root.glob("*.md"):
            if path.name.startswith("theme_"):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            theme = path.stem.replace("_", " ")
            for ticker in tickers:
                if f"- {ticker} " in text or f"- {ticker} -" in text:
                    output.setdefault(ticker, []).append(theme)
        return output

    def _patterns_by_ticker(self) -> dict[str, list[str]]:
        output: dict[str, list[str]] = {}
        root = self.repo_root / "reports" / "patterns"
        if not root.exists():
            return output
        tickers = self._known_tickers()
        for path in root.glob("*patterns.md"):
            text = path.read_text(encoding="utf-8", errors="ignore")
            label = path.stem.replace("_", " ")
            for ticker in tickers:
                if ticker in text:
                    output.setdefault(ticker, []).append(label)
        return output

    def _known_tickers(self) -> set[str]:
        price_root = self.repo_root / "storage" / "raw" / "prices"
        return {path.stem.upper() for path in price_root.glob("*.csv")} if price_root.exists() else set()

    def _benchmark_return(self, signal_date: date) -> float | None:
        holding_days = int(self.config.get("sell", {}).get("holding_days", 180))
        end_date = signal_date.replace()  # keep the date object explicit for readability
        from datetime import timedelta

        end_date = end_date + timedelta(days=holding_days)
        values = []
        for ticker in self.config.get("benchmarks", {}).values():
            prices = self._price_rows(str(ticker))
            start = self._price_on_or_before(prices, signal_date)
            end = self._price_on_or_before(prices, end_date)
            start_price = adjusted_close(start) if start else None
            end_price = adjusted_close(end) if end else None
            if start_price not in (None, 0) and end_price is not None:
                values.append(round((end_price - start_price) / start_price * 100, 2))
        return round(sum(values) / len(values), 2) if values else None

    def _price_rows(self, ticker: str) -> list[dict[str, str]]:
        path = self.repo_root / "storage" / "raw" / "prices" / f"{ticker.upper()}.csv"
        if not path.exists():
            return []
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))

    def _price_on_or_before(self, prices: list[dict[str, str]], target: date) -> dict[str, str] | None:
        for row in reversed(prices):
            try:
                if date.fromisoformat(row["date"]) <= target:
                    return row
            except (KeyError, ValueError):
                continue
        return None
