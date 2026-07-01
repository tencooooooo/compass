import csv
from typing import Any

from api.services.data_loader import REPO_ROOT, list_json_files, read_json


class PatternExtractor:
    """Extracts company-level features from Compass generated data."""

    def extract(self) -> dict[str, Any]:
        tickers = self._tickers()
        validation = self._validation_by_ticker()
        market = read_json("reports/market/market_dashboard.json", {})
        return {
            "companies": {ticker: self._company_features(ticker, validation.get(ticker, []), market) for ticker in tickers},
            "discovery_history": self._discovery_history(),
            "validation": validation,
            "market": market,
            "time_machine": self._time_machine_reports(),
            "learning": read_json("memory/learning/learning_history.json", []),
            "memory": self._company_memory(),
        }

    def _tickers(self) -> list[str]:
        tickers = {path.stem.upper() for path in list_json_files("storage/raw/companies")}
        tickers.update(path.stem.upper() for path in list_json_files("storage/raw/financials"))
        return sorted(tickers)

    def _company_features(self, ticker: str, validation_rows: list[dict[str, Any]], market: dict[str, Any]) -> dict[str, Any]:
        company = read_json(f"storage/raw/companies/{ticker}.json", {})
        financials = read_json(f"storage/raw/financials/{ticker}.json", {})
        news = read_json(f"storage/raw/news/{ticker}.json", [])
        events = read_json(f"storage/events/{ticker}_events.json", [])
        prices = self._prices(ticker)
        sector = company.get("sector") or "Unknown"
        return {
            "ticker": ticker,
            "company_name": company.get("company_name"),
            "sector": sector,
            "industry": company.get("industry"),
            "financials": {
                "rd_ratio": self._ratio(financials.get("research_and_development"), financials.get("total_revenue")),
                "profit_margin": financials.get("profit_margin"),
                "operating_margin": financials.get("operating_margin"),
                "eps": financials.get("eps"),
                "free_cash_flow": financials.get("free_cash_flow"),
                "trailing_pe": company.get("trailing_pe"),
                "current_ratio": financials.get("current_ratio"),
            },
            "market": {
                "sector_trend": self._sector_trend(sector, market),
                "sector_average_score": self._sector_value(sector, market, "average_score"),
                "sector_average_momentum_1m": self._sector_value(sector, market, "average_momentum_1m"),
            },
            "activity": {
                "news_count": len(news) if isinstance(news, list) else 0,
                "event_count": len(events) if isinstance(events, list) else 0,
                "price_count": len(prices),
                "momentum_1m": self._momentum(prices, 22),
                "momentum_3m": self._momentum(prices, 63),
            },
            "validation": {
                "results": self._result_counts(validation_rows),
                "average_return": self._average_return(validation_rows),
                "completed_count": sum(1 for row in validation_rows if row.get("period_complete")),
            },
        }

    def _validation_by_ticker(self) -> dict[str, list[dict[str, Any]]]:
        rows = read_json("reports/validation/validation_history.json", [])
        output: dict[str, list[dict[str, Any]]] = {}
        if not isinstance(rows, list):
            return output
        for row in rows:
            ticker = str(row.get("ticker", "")).upper()
            if ticker:
                output.setdefault(ticker, []).append(row)
        return output

    def _company_memory(self) -> dict[str, Any]:
        return {path.stem.upper(): read_json(f"memory/companies/{path.name}", {}) for path in list_json_files("memory/companies")}

    def _time_machine_reports(self) -> list[str]:
        path = REPO_ROOT / "reports" / "timemachine"
        if not path.exists():
            return []
        return sorted(item.name for item in path.glob("*.md"))

    def _discovery_history(self) -> dict[str, Any]:
        history = {path.stem: read_json(f"memory/discoveries/{path.name}", {}) for path in list_json_files("memory/discoveries")}
        latest = read_json("reports/discovery/discovery_candidates.json", {})
        if latest:
            history["latest_report"] = latest
        return history

    def _prices(self, ticker: str) -> list[dict[str, str]]:
        price_root = REPO_ROOT / "storage" / "raw" / "prices"
        csv_path = price_root / f"{ticker}.csv"
        if csv_path is None:
            return []
        if not csv_path.exists():
            return []
        with csv_path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))

    def _momentum(self, prices: list[dict[str, str]], window: int) -> float | None:
        if len(prices) <= window:
            return None
        try:
            latest = float(prices[-1]["close"])
            previous = float(prices[-window - 1]["close"])
        except (KeyError, TypeError, ValueError):
            return None
        if previous == 0:
            return None
        return round((latest - previous) / previous * 100, 2)

    def _ratio(self, numerator: Any, denominator: Any) -> float | None:
        try:
            if denominator in (None, 0):
                return None
            return round(float(numerator) / float(denominator), 4)
        except (TypeError, ValueError):
            return None

    def _result_counts(self, rows: list[dict[str, Any]]) -> dict[str, int]:
        counts = {"Excellent": 0, "Good": 0, "Neutral": 0, "Poor": 0}
        for row in rows:
            result = row.get("validation_result")
            if result in counts:
                counts[result] += 1
        return counts

    def _average_return(self, rows: list[dict[str, Any]]) -> float | None:
        values = [row.get("return_percent") for row in rows if isinstance(row.get("return_percent"), (int, float))]
        return round(sum(values) / len(values), 2) if values else None

    def _sector_trend(self, sector: str, market: dict[str, Any]) -> dict[str, Any]:
        for item in market.get("sectors", []) if isinstance(market, dict) else []:
            if item.get("sector") == sector:
                return item.get("trend", {})
        return {}

    def _sector_value(self, sector: str, market: dict[str, Any], key: str) -> Any:
        for item in market.get("sectors", []) if isinstance(market, dict) else []:
            if item.get("sector") == sector:
                return item.get(key)
        return None
