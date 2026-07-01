from statistics import mean
from typing import Any

from api.services.data_loader import read_json


class ThemeTracker:
    """Aggregates theme-level scores, Discovery, market context, and validation results."""

    def track(self, classified: dict[str, Any]) -> dict[str, Any]:
        scores = self._scores()
        discovery = self._discovery()
        validation = self._validation()
        market = read_json("reports/market/market_dashboard.json", {})
        output = {}
        for theme, payload in classified.items():
            companies = payload.get("companies", [])
            tickers = [item["ticker"] for item in companies]
            output[theme] = {
                "companies": companies,
                "company_count": len(companies),
                "average_score": self._average([scores.get(ticker, {}).get("total_score") for ticker in tickers]),
                "average_discovery": self._average([discovery.get(ticker, {}).get("discovery_score") for ticker in tickers]),
                "market_status": self._market_status(companies, market),
                "representative_companies": self._representatives(tickers, scores, discovery),
                "major_news": self._major_news(tickers),
                "validation": self._validation_summary(tickers, validation),
                "momentum": self._momentum(tickers, discovery, market),
                "confidence": self._confidence(companies),
            }
        return output

    def ranking(self, themes: dict[str, Any]) -> list[dict[str, Any]]:
        rows = []
        for theme, item in themes.items():
            discovery_count = sum(1 for company in item.get("companies", []) if company.get("ticker"))
            validation_good = item.get("validation", {}).get("Excellent", 0) + item.get("validation", {}).get("Good", 0)
            momentum = item.get("momentum", {}).get("average_1m")
            rank_score = self._num(item.get("average_score")) + self._num(item.get("average_discovery"))
            rank_score += self._num(momentum) + validation_good * 3 + discovery_count
            rows.append(
                {
                    "theme": theme,
                    "momentum": momentum,
                    "discovery_count": discovery_count,
                    "validation": item.get("validation", {}),
                    "rank_score": round(rank_score, 2),
                }
            )
        return sorted(rows, key=lambda row: row["rank_score"], reverse=True)

    def _scores(self) -> dict[str, dict[str, Any]]:
        data = read_json("reports/scoring/company_scores.json", {})
        rows = data.get("results", []) if isinstance(data, dict) else []
        return {str(row.get("ticker", "")).upper(): row for row in rows if isinstance(row, dict)}

    def _discovery(self) -> dict[str, dict[str, Any]]:
        data = read_json("reports/discovery/discovery_candidates.json", {})
        rows = data.get("candidates", []) if isinstance(data, dict) else []
        return {str(row.get("ticker", "")).upper(): row for row in rows if isinstance(row, dict)}

    def _validation(self) -> dict[str, list[dict[str, Any]]]:
        rows = read_json("reports/validation/validation_history.json", [])
        output: dict[str, list[dict[str, Any]]] = {}
        if not isinstance(rows, list):
            return output
        for row in rows:
            ticker = str(row.get("ticker", "")).upper()
            if ticker:
                output.setdefault(ticker, []).append(row)
        return output

    def _major_news(self, tickers: list[str]) -> list[dict[str, str]]:
        news = []
        for ticker in tickers:
            rows = read_json(f"storage/raw/news/{ticker}.json", [])
            if isinstance(rows, list):
                for row in rows[:3]:
                    if isinstance(row, dict) and row.get("title"):
                        news.append({"ticker": ticker, "title": row["title"], "published_at": row.get("published_at", "")})
        return sorted(news, key=lambda item: item.get("published_at", ""), reverse=True)[:5]

    def _market_status(self, companies: list[dict[str, Any]], market: dict[str, Any]) -> list[dict[str, Any]]:
        sectors = {company.get("sector") for company in companies if company.get("sector")}
        rows = market.get("sectors", []) if isinstance(market, dict) else []
        return [row for row in rows if row.get("sector") in sectors]

    def _representatives(self, tickers: list[str], scores: dict[str, Any], discovery: dict[str, Any]) -> list[dict[str, Any]]:
        rows = []
        for ticker in tickers:
            rows.append(
                {
                    "ticker": ticker,
                    "company_name": scores.get(ticker, {}).get("company_name") or discovery.get(ticker, {}).get("company") or ticker,
                    "score": scores.get(ticker, {}).get("total_score"),
                    "discovery_score": discovery.get(ticker, {}).get("discovery_score"),
                }
            )
        return sorted(rows, key=lambda row: (self._num(row.get("discovery_score")), self._num(row.get("score"))), reverse=True)[:5]

    def _validation_summary(self, tickers: list[str], validation: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
        counts = {"Excellent": 0, "Good": 0, "Neutral": 0, "Poor": 0}
        returns = []
        for ticker in tickers:
            for row in validation.get(ticker, []):
                result = row.get("validation_result")
                if result in counts:
                    counts[result] += 1
                if isinstance(row.get("return_percent"), (int, float)):
                    returns.append(row["return_percent"])
        counts["average_return"] = round(mean(returns), 2) if returns else None
        return counts

    def _momentum(self, tickers: list[str], discovery: dict[str, Any], market: dict[str, Any]) -> dict[str, Any]:
        values = []
        for ticker in tickers:
            momentum = discovery.get(ticker, {}).get("metrics", {}).get("momentum", {}).get("1m")
            if isinstance(momentum, (int, float)):
                values.append(momentum)
        sector_values = []
        for sector in market.get("sectors", []) if isinstance(market, dict) else []:
            if isinstance(sector.get("average_momentum_1m"), (int, float)):
                sector_values.append(sector["average_momentum_1m"])
        return {
            "average_1m": round(mean(values), 2) if values else None,
            "market_average_1m": round(mean(sector_values), 2) if sector_values else None,
        }

    def _confidence(self, companies: list[dict[str, Any]]) -> str:
        levels = [item.get("confidence") for item in companies]
        if levels.count("High") >= 2 or (levels and all(level == "High" for level in levels)):
            return "High"
        if levels:
            return "Medium"
        return "Low"

    def _average(self, values: list[Any]) -> float | None:
        numeric = [float(value) for value in values if isinstance(value, (int, float))]
        return round(mean(numeric), 2) if numeric else None

    def _num(self, value: Any) -> float:
        try:
            return float(value or 0)
        except (TypeError, ValueError):
            return 0.0
