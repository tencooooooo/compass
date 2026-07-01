from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Any


# このファイル(core/memory/memory_engine.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.memory.local_provider import LocalProvider  # noqa: E402
from core.memory.memory_provider import MemoryProvider  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402


SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
MEMORY_ROOT = PROJECT_ROOT / "memory"


class Memory:
    """他EngineがProviderを意識せず使うためのMemory APIです。"""

    _provider: MemoryProvider = LocalProvider(MEMORY_ROOT)

    @classmethod
    def configure(cls, provider: MemoryProvider) -> None:
        cls._provider = provider

    @classmethod
    def save(cls, collection: str, key: str, data: dict[str, Any]) -> None:
        cls._provider.save(collection, key, data)

    @classmethod
    def load(cls, collection: str, key: str, default: Any = None) -> Any:
        return cls._provider.load(collection, key, default)

    @classmethod
    def update(cls, collection: str, key: str, updates: dict[str, Any]) -> dict[str, Any]:
        return cls._provider.update(collection, key, updates)

    @classmethod
    def delete(cls, collection: str, key: str) -> bool:
        return cls._provider.delete(collection, key)

    @classmethod
    def exists(cls, collection: str, key: str) -> bool:
        return cls._provider.exists(collection, key)

    @classmethod
    def list(cls, collection: str) -> list[str]:
        return cls._provider.list(collection)

    @classmethod
    def search(cls, collection: str, query: str, limit: int = 20) -> list[dict[str, Any]]:
        return cls._provider.search(collection, query, limit)


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def safe_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def safe_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def replace_daily_snapshot(history: list[dict[str, Any]], snapshot: dict[str, Any], date_key: str) -> list[dict[str, Any]]:
    filtered = [item for item in history if item.get("date") != date_key]
    filtered.append(snapshot)
    return sorted(filtered, key=lambda item: item.get("date", ""))


def scoring_by_ticker() -> dict[str, dict[str, Any]]:
    data = load_json(PROJECT_ROOT / "reports" / "scoring" / "company_scores.json", {})
    return {
        str(item.get("ticker")).upper(): item
        for item in safe_list(data.get("results"))
        if isinstance(item, dict) and item.get("ticker")
    }


def discovery_by_ticker() -> dict[str, dict[str, Any]]:
    data = load_json(PROJECT_ROOT / "reports" / "discovery" / "discovery_candidates.json", {})
    candidates = safe_list(data.get("candidates")) + safe_list(data.get("all_companies"))
    result: dict[str, dict[str, Any]] = {}
    for item in candidates:
        if isinstance(item, dict) and item.get("ticker"):
            result[str(item["ticker"]).upper()] = item
    return result


def validation_by_ticker() -> dict[str, list[dict[str, Any]]]:
    rows = load_json(PROJECT_ROOT / "reports" / "validation" / "validation_history.json", [])
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in safe_list(rows):
        ticker = str(row.get("ticker") or "").upper()
        if ticker:
            grouped[ticker].append(row)
    return dict(grouped)


def company_profiles() -> dict[str, dict[str, Any]]:
    companies: dict[str, dict[str, Any]] = {}
    company_dir = PROJECT_ROOT / "storage" / "raw" / "companies"
    for path in company_dir.glob("*.json"):
        data = load_json(path, {})
        ticker = str(data.get("ticker") or path.stem).upper()
        companies[ticker] = data
    return companies


def latest_items(items: list[dict[str, Any]], limit: int = 10) -> list[dict[str, Any]]:
    return sorted(items, key=lambda item: str(item.get("published_at") or item.get("date") or ""), reverse=True)[:limit]


def build_company_memory(timestamp: str, date_key: str) -> int:
    companies = company_profiles()
    scores = scoring_by_ticker()
    discoveries = discovery_by_ticker()
    validations = validation_by_ticker()
    tickers = sorted(set(companies) | set(scores) | set(discoveries) | set(validations))

    for ticker in tickers:
        company = companies.get(ticker, {"ticker": ticker})
        score = scores.get(ticker, {})
        discovery = discoveries.get(ticker, {})
        validation_rows = validations.get(ticker, [])
        events = safe_list(load_json(PROJECT_ROOT / "storage" / "events" / f"{ticker}_events.json", []))
        news = safe_list(load_json(PROJECT_ROOT / "storage" / "raw" / "news" / f"{ticker}.json", []))
        confidence = {
            "scoring": (score.get("confidence") or {}).get("level") if isinstance(score.get("confidence"), dict) else None,
            "discovery": discovery.get("confidence"),
        }
        snapshot = {
            "date": date_key,
            "timestamp": timestamp,
            "score": score.get("total_score"),
            "discovery_score": discovery.get("discovery_score"),
            "discovery_status": discovery.get("status"),
            "validation_results": Counter(row.get("validation_result") for row in validation_rows),
            "event_count": len(events),
            "news_count": len(news),
            "confidence": confidence,
        }
        existing = Memory.load("companies", ticker, default={})
        history = safe_list(existing.get("History")) if isinstance(existing, dict) else []
        payload = {
            "Company": company,
            "History": replace_daily_snapshot(history, snapshot, date_key),
            "Scores": score,
            "Discovery": discovery,
            "Validation": validation_rows,
            "Events": {"count": len(events), "latest": latest_items(events)},
            "News": {"count": len(news), "latest": latest_items(news)},
            "Confidence": confidence,
            "Timestamp": timestamp,
        }
        Memory.save("companies", ticker, payload)
    return len(tickers)


def build_sector_memory(timestamp: str, date_key: str) -> int:
    market_data = load_json(PROJECT_ROOT / "reports" / "market" / "market_dashboard.json", {})
    sectors = safe_list(market_data.get("sectors"))
    discoveries = discovery_by_ticker()
    validations = validation_by_ticker()
    companies = company_profiles()
    top_events = safe_list(market_data.get("top_events"))

    for sector in sectors:
        sector_name = sector.get("sector")
        if not sector_name:
            continue
        tickers = [ticker for ticker, company in companies.items() if company.get("sector") == sector_name]
        validation_rows = [row for ticker in tickers for row in validations.get(ticker, [])]
        discovery_count = sum(1 for ticker in tickers if ticker in discoveries)
        result_counts = Counter(row.get("validation_result") for row in validation_rows)
        major_news = [event for event in top_events if event.get("ticker") in tickers][:5]
        snapshot = {
            "date": date_key,
            "timestamp": timestamp,
            "average_score": sector.get("average_score"),
            "average_momentum_1m": sector.get("average_momentum_1m"),
            "discovery_count": discovery_count,
            "validation_results": result_counts,
        }
        existing = Memory.load("sectors", sector_name, default={})
        history = safe_list(existing.get("History")) if isinstance(existing, dict) else []
        payload = {
            "Sector": sector_name,
            "History": replace_daily_snapshot(history, snapshot, date_key),
            "AverageScore": sector.get("average_score"),
            "AverageMomentum": {
                "1m": sector.get("average_momentum_1m"),
            },
            "MajorNews": major_news,
            "DiscoveryCount": discovery_count,
            "ValidationResults": dict(result_counts),
            "Timestamp": timestamp,
        }
        Memory.save("sectors", sector_name, payload)
    return len(sectors)


def build_discovery_memory(timestamp: str, date_key: str) -> None:
    data = load_json(PROJECT_ROOT / "reports" / "discovery" / "discovery_candidates.json", {})
    payload = {
        "date": date_key,
        "timestamp": timestamp,
        "generated_at": data.get("generated_at"),
        "candidates": [
            {
                "ticker": item.get("ticker"),
                "company": item.get("company"),
                "score": item.get("discovery_score"),
                "confidence": item.get("confidence"),
                "reasons": item.get("discovery_reasons"),
                "status": item.get("status"),
            }
            for item in safe_list(data.get("candidates"))
        ],
    }
    Memory.save("discoveries", date_key, payload)


def build_validation_memory(timestamp: str, month_key: str) -> None:
    rows = safe_list(load_json(PROJECT_ROOT / "reports" / "validation" / "validation_history.json", []))
    month_rows = [row for row in rows if str(row.get("validation_date") or "").startswith(month_key)]
    returns = [safe_float(row.get("return_percent")) for row in month_rows]
    returns = [value for value in returns if value is not None]
    counts = Counter(row.get("validation_result") for row in month_rows)
    payload = {
        "month": month_key,
        "timestamp": timestamp,
        "Excellent": counts.get("Excellent", 0),
        "Good": counts.get("Good", 0),
        "Neutral": counts.get("Neutral", 0),
        "Poor": counts.get("Poor", 0),
        "average_return": sum(returns) / len(returns) if returns else None,
        "rows": month_rows,
    }
    Memory.save("validations", month_key, payload)


def build_market_memory(timestamp: str, date_key: str) -> None:
    data = load_json(PROJECT_ROOT / "reports" / "market" / "market_dashboard.json", {})
    Memory.save(
        "market",
        date_key,
        {
            "date": date_key,
            "timestamp": timestamp,
            "market": data.get("market", {}),
            "sectors": data.get("sectors", []),
            "top_events": data.get("top_events", []),
            "summary": data.get("summary", {}),
        },
    )


def build_lessons_memory(timestamp: str) -> None:
    if Memory.exists("lessons", "lessons"):
        return
    Memory.save(
        "lessons",
        "lessons",
        {
            "Timestamp": timestamp,
            "Purpose": "Learning Engineが将来、検証結果から得た知見を蓄積する場所です。",
            "Lessons": [],
            "Template": {
                "date": "YYYY-MM-DD",
                "observation": "",
                "related_tickers": [],
                "what_worked": [],
                "what_did_not_work": [],
                "rule_update_candidate": "",
                "human_review": "",
            },
        },
    )


def main() -> int:
    settings = load_yaml(SETTINGS_PATH)
    logger = setup_logger(PROJECT_ROOT, settings, "compass.memory")
    timezone = get_timezone(settings)
    now = datetime.now(timezone)
    timestamp = now.isoformat()
    date_key = now.strftime("%Y-%m-%d")
    month_key = now.strftime("%Y-%m")

    logger.info("Compass Core 01 - Memory Engine")
    logger.info("開始時刻: %s", now.strftime("%Y-%m-%d %H:%M:%S"))

    Memory.configure(LocalProvider(MEMORY_ROOT))
    company_count = build_company_memory(timestamp, date_key)
    sector_count = build_sector_memory(timestamp, date_key)
    build_discovery_memory(timestamp, date_key)
    build_validation_memory(timestamp, month_key)
    build_market_memory(timestamp, date_key)
    build_lessons_memory(timestamp)

    logger.info("Company Memory保存: %s 件", company_count)
    logger.info("Sector Memory保存: %s 件", sector_count)
    logger.info("保存先: %s", MEMORY_ROOT)
    logger.info("終了時刻: %s", datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
