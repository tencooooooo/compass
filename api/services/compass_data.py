from functools import lru_cache
from pathlib import Path
import re
from typing import Any

from api.services.data_loader import list_json_files, read_json, read_text


def _ticker(value: str) -> str:
    ticker = value.upper().strip()
    if not re.fullmatch(r"[A-Z0-9.\-^]{1,10}", ticker):
        raise ValueError(f"Invalid ticker: {value}")
    return ticker


@lru_cache(maxsize=1)
def _score_results() -> list[dict[str, Any]]:
    scoring = read_json("reports/scoring/company_scores.json", {})
    return scoring.get("results", []) if isinstance(scoring, dict) else []


def _score_by_ticker(ticker: str) -> dict[str, Any] | None:
    target = _ticker(ticker)
    for score in _score_results():
        if _ticker(str(score.get("ticker", ""))) == target:
            return score
    return None


@lru_cache(maxsize=1)
def _discovery_candidates() -> list[dict[str, Any]]:
    discovery = read_json("reports/discovery/discovery_candidates.json", {})
    if not isinstance(discovery, dict):
        return []
    candidates = discovery.get("candidates", [])
    return candidates if isinstance(candidates, list) else []


def _discovery_by_ticker(ticker: str) -> dict[str, Any] | None:
    target = _ticker(ticker)
    for candidate in _discovery_candidates():
        if _ticker(str(candidate.get("ticker", ""))) == target:
            return candidate
    return None


@lru_cache(maxsize=1)
def _validation_rows() -> list[dict[str, Any]]:
    validation = read_json("reports/validation/validation_history.json", [])
    return validation if isinstance(validation, list) else []


def _validation_by_ticker(ticker: str) -> list[dict[str, Any]]:
    target = _ticker(ticker)
    return [row for row in _validation_rows() if _ticker(str(row.get("ticker", ""))) == target]


def _latest_validation(ticker: str) -> dict[str, Any] | None:
    rows = _validation_by_ticker(ticker)
    if not rows:
        return None
    return sorted(rows, key=lambda row: str(row.get("validation_date", "")), reverse=True)[0]


def _read_company_file(path: Path) -> dict[str, Any] | None:
    data = read_json(str(path.relative_to(path.parents[3])), None)
    return data if isinstance(data, dict) else None


def get_companies() -> list[dict[str, Any]]:
    companies: list[dict[str, Any]] = []
    for path in list_json_files("storage/raw/companies"):
        company = _read_company_file(path)
        if not company:
            continue
        ticker = str(company.get("ticker", path.stem))
        companies.append(
            {
                "ticker": ticker,
                "company_name": company.get("company_name"),
                "sector": company.get("sector"),
                "industry": company.get("industry"),
                "country": company.get("country"),
                "market_cap": company.get("market_cap"),
                "latest_score": _score_by_ticker(ticker),
                "latest_discovery": _discovery_by_ticker(ticker),
                "latest_validation": _latest_validation(ticker),
            }
        )
    return companies


def get_company(ticker: str) -> dict[str, Any] | None:
    target = _ticker(ticker)
    company = read_json(f"storage/raw/companies/{target}.json", None)
    if not isinstance(company, dict):
        return None
    return {
        "profile": company,
        "latest_score": _score_by_ticker(target),
        "latest_discovery": _discovery_by_ticker(target),
        "latest_validation": _latest_validation(target),
        "report_markdown": read_text(f"reports/company_analysis/{target}.md"),
    }


def get_discovery() -> dict[str, Any]:
    return read_json("reports/discovery/discovery_candidates.json", {"candidates": []})


def get_top_discovery(limit: int = 3) -> list[dict[str, Any]]:
    return sorted(_discovery_candidates(), key=lambda item: item.get("discovery_score", 0), reverse=True)[:limit]


def get_scores() -> dict[str, Any]:
    return read_json("reports/scoring/company_scores.json", {"results": []})


def get_score(ticker: str) -> dict[str, Any] | None:
    return _score_by_ticker(ticker)


def get_market() -> dict[str, Any]:
    return read_json("reports/market/market_dashboard.json", {})


def get_market_sectors() -> list[dict[str, Any]]:
    market = get_market()
    sectors = market.get("sectors", []) if isinstance(market, dict) else []
    return sectors if isinstance(sectors, list) else []


def get_validation() -> list[dict[str, Any]]:
    return _validation_rows()


def get_validation_for_ticker(ticker: str) -> list[dict[str, Any]]:
    return _validation_by_ticker(ticker)


def get_proposals() -> list[dict[str, Any]]:
    proposals = read_json("reports/proposals/proposal_index.json", [])
    return proposals if isinstance(proposals, list) else []


def get_learning() -> dict[str, Any]:
    return {
        "metrics": read_json("reports/learning/learning_metrics.json", {}),
        "summary_markdown": read_text("reports/learning/learning_summary.md"),
        "history": read_json("memory/learning/learning_history.json", []),
    }


def get_notifications() -> list[dict[str, Any]]:
    notifications = read_json("storage/notifications/notification_history.json", [])
    return notifications if isinstance(notifications, list) else []
