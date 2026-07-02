from functools import lru_cache
import json
from pathlib import Path
import re
from typing import Any

from api.services.data_loader import list_json_files, read_json, read_text, resolve_path


TICKER_PATTERN = re.compile(r"[A-Z0-9.\-^]{1,10}")


def validate_ticker(value: str) -> str:
    """Validate user-supplied ticker values before using them in file paths."""
    ticker = value.upper().strip()
    if not TICKER_PATTERN.fullmatch(ticker):
        raise ValueError(f"Invalid ticker: {value}")
    return ticker


def normalize_ticker(value: Any) -> str | None:
    """Normalize generated-data ticker values; invalid rows are ignored."""
    ticker = str(value or "").upper().strip()
    return ticker if TICKER_PATTERN.fullmatch(ticker) else None


def _file_mtime(relative_path: str) -> float:
    path = resolve_path(relative_path)
    return path.stat().st_mtime if path.exists() else 0.0


@lru_cache(maxsize=32)
def _read_json_by_mtime(relative_path: str, modified_at: float, fallback_repr: str) -> Any:
    fallback = [] if fallback_repr == "list" else {}
    path = resolve_path(relative_path)
    if not path.exists():
        return fallback
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return fallback


def _score_results() -> list[dict[str, Any]]:
    path = "reports/scoring/company_scores.json"
    scoring = _read_json_by_mtime(path, _file_mtime(path), "dict")
    return scoring.get("results", []) if isinstance(scoring, dict) else []


def _score_by_ticker(ticker: str) -> dict[str, Any] | None:
    target = validate_ticker(ticker)
    for score in _score_results():
        if normalize_ticker(score.get("ticker")) == target:
            return score
    return None


def _discovery_candidates() -> list[dict[str, Any]]:
    path = "reports/discovery/discovery_candidates.json"
    discovery = _read_json_by_mtime(path, _file_mtime(path), "dict")
    if not isinstance(discovery, dict):
        return []
    candidates = discovery.get("candidates", [])
    return candidates if isinstance(candidates, list) else []


def _discovery_by_ticker(ticker: str) -> dict[str, Any] | None:
    target = validate_ticker(ticker)
    for candidate in _discovery_candidates():
        if normalize_ticker(candidate.get("ticker")) == target:
            return candidate
    return None


def _validation_rows() -> list[dict[str, Any]]:
    path = "reports/validation/validation_history.json"
    validation = _read_json_by_mtime(path, _file_mtime(path), "list")
    return validation if isinstance(validation, list) else []


def _validation_by_ticker(ticker: str) -> list[dict[str, Any]]:
    target = validate_ticker(ticker)
    return [row for row in _validation_rows() if normalize_ticker(row.get("ticker")) == target]


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
        lookup_ticker = normalize_ticker(ticker)
        companies.append(
            {
                "ticker": ticker,
                "company_name": company.get("company_name"),
                "sector": company.get("sector"),
                "industry": company.get("industry"),
                "country": company.get("country"),
                "market_cap": company.get("market_cap"),
                "latest_score": _score_by_ticker(lookup_ticker) if lookup_ticker else None,
                "latest_discovery": _discovery_by_ticker(lookup_ticker) if lookup_ticker else None,
                "latest_validation": _latest_validation(lookup_ticker) if lookup_ticker else None,
            }
        )
    return companies


def get_company(ticker: str) -> dict[str, Any] | None:
    target = validate_ticker(ticker)
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
