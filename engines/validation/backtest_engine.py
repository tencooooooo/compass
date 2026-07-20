from __future__ import annotations

from datetime import datetime
from functools import lru_cache
import json
from pathlib import Path
import sys
from typing import Any

import pandas as pd


# このファイル(engines/validation/backtest_engine.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]

from engines.validation.performance_tracker import save_history  # noqa: E402
from engines.validation.thresholds import (  # noqa: E402
    VALIDATION_PERIODS,
    VALIDATION_THRESHOLDS,
    classify_result,
    threshold_note,
)
from engines.validation.validation_report import render_validation_summary  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.price_data import adjusted_close, normalize_price_frame  # noqa: E402
from utils.tickers import load_sector_benchmarks  # noqa: E402


SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
TICKERS_CONFIG_PATH = PROJECT_ROOT / "config" / "tickers.yaml"
DISCOVERY_PATH = PROJECT_ROOT / "reports" / "discovery" / "discovery_candidates.json"
DISCOVERY_MEMORY_DIR = PROJECT_ROOT / "memory" / "discoveries"
VALIDATION_MEMORY_DIR = PROJECT_ROOT / "memory" / "validations"
REPORT_DIR = PROJECT_ROOT / "reports" / "validation"
PRICE_DIR = PROJECT_ROOT / "storage" / "raw" / "prices"
COMPANY_DIR = PROJECT_ROOT / "storage" / "raw" / "companies"
EVENT_DIR = PROJECT_ROOT / "storage" / "events"

BENCHMARK_CANDIDATES = ["SPY", "^GSPC"]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def normalize_memory_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    """Convert the compact Discovery Memory schema to the live report schema."""
    normalized = dict(candidate)
    normalized.setdefault("discovery_score", candidate.get("score"))
    normalized.setdefault("discovery_reasons", candidate.get("reasons", []))
    return normalized


def discovery_snapshots(timezone) -> list[tuple[datetime, list[dict[str, Any]]]]:
    """Load every durable Discovery snapshot and overlay today's live report."""
    snapshots: dict[str, tuple[datetime, list[dict[str, Any]]]] = {}
    if DISCOVERY_MEMORY_DIR.exists():
        for path in sorted(DISCOVERY_MEMORY_DIR.glob("*.json")):
            data = load_json(path, {})
            if not isinstance(data, dict):
                continue
            candidates = [normalize_memory_candidate(item) for item in data.get("candidates", []) if isinstance(item, dict)]
            if not candidates:
                continue
            generated_at = data.get("date") or data.get("generated_at") or data.get("timestamp")
            parsed = parse_datetime(str(generated_at) if generated_at else None, timezone)
            snapshots[parsed.date().isoformat()] = (parsed, candidates)

    live = load_json(DISCOVERY_PATH, {})
    live_candidates = live.get("candidates", []) if isinstance(live, dict) else []
    if live_candidates:
        parsed = parse_datetime(live.get("generated_at"), timezone)
        snapshots[parsed.date().isoformat()] = (parsed, [item for item in live_candidates if isinstance(item, dict)])
    return [snapshots[key] for key in sorted(snapshots)]


def validation_memory_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not VALIDATION_MEMORY_DIR.exists():
        return rows
    for path in sorted(VALIDATION_MEMORY_DIR.glob("*.json")):
        data = load_json(path, {})
        if isinstance(data, dict):
            rows.extend(item for item in data.get("rows", []) if isinstance(item, dict))
    return rows


@lru_cache(maxsize=None)
def load_prices(ticker: str) -> pd.DataFrame:
    path = PRICE_DIR / f"{ticker}.csv"
    if not path.exists():
        return pd.DataFrame()
    prices = pd.read_csv(path)
    if prices.empty or "date" not in prices.columns or "close" not in prices.columns:
        return pd.DataFrame()
    return normalize_price_frame(prices)


def parse_datetime(value: str | None, timezone) -> datetime:
    if not value:
        return datetime.now(timezone)
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone)
    return parsed.astimezone(timezone)


def price_on_or_before(prices: pd.DataFrame, target_date: pd.Timestamp) -> pd.Series | None:
    candidates = prices[prices["date"] <= target_date]
    if candidates.empty:
        return None
    return candidates.iloc[-1]


def price_on_or_after(prices: pd.DataFrame, target_date: pd.Timestamp) -> tuple[pd.Series | None, bool]:
    candidates = prices[prices["date"] >= target_date]
    if not candidates.empty:
        return candidates.iloc[0], True
    if prices.empty:
        return None, False
    return prices.iloc[-1], False


def calculate_return(prices: pd.DataFrame, discovery_date: datetime, period_days: int) -> dict[str, Any]:
    prices = normalize_price_frame(prices)
    if prices.empty:
        return {
            "start_date": None,
            "end_date": None,
            "start_price": None,
            "end_price": None,
            "return_percent": None,
            "period_complete": False,
        }

    discovery_ts = pd.Timestamp(discovery_date.date())
    start_row = price_on_or_before(prices, discovery_ts)
    if start_row is None:
        start_row = prices.iloc[0]
        if (pd.Timestamp(start_row["date"]) - discovery_ts).days > 7:
            return {
                "start_date": pd.Timestamp(start_row["date"]).date().isoformat(),
                "end_date": None,
                "start_price": adjusted_close(start_row),
                "end_price": None,
                "return_percent": None,
                "period_complete": False,
            }
    target_end = pd.Timestamp(start_row["date"]) + pd.Timedelta(days=period_days)
    end_row, complete = price_on_or_after(prices, target_end)
    if end_row is None:
        end_row = start_row
        complete = False

    start_price = adjusted_close(start_row)
    end_price = adjusted_close(end_row)
    if start_price is None or end_price is None:
        return_percent = None
    else:
        return_percent = None if start_price == 0 else ((end_price - start_price) / start_price) * 100
    return {
        "start_date": pd.Timestamp(start_row["date"]).date().isoformat(),
        "end_date": pd.Timestamp(end_row["date"]).date().isoformat(),
        "start_price": start_price,
        "end_price": end_price,
        "return_percent": return_percent,
        "period_complete": bool(complete),
    }


@lru_cache(maxsize=None)
def ticker_period_return(ticker: str, discovery_date_iso: str, period_days: int) -> dict[str, Any]:
    """同じ銘柄・Discovery日・期間の再計算をキャッシュします(ピア平均で同一計算が候補数×期間分繰り返されるため)。"""
    return calculate_return(load_prices(ticker), datetime.fromisoformat(discovery_date_iso), period_days)


def load_benchmark() -> tuple[str | None, pd.DataFrame]:
    for ticker in BENCHMARK_CANDIDATES:
        prices = load_prices(ticker)
        if not prices.empty:
            return ticker, prices
    return None, pd.DataFrame()


def companies_by_ticker() -> dict[str, dict[str, Any]]:
    companies: dict[str, dict[str, Any]] = {}
    for path in COMPANY_DIR.glob("*.json"):
        data = load_json(path, {})
        ticker = str(data.get("ticker") or path.stem).upper()
        companies[ticker] = data
    return companies


def sector_returns(
    ticker: str,
    sector: str | None,
    companies: dict[str, dict[str, Any]],
    discovery_date: datetime,
    period_days: int,
) -> float | None:
    if not sector:
        return None
    returns: list[float] = []
    discovery_iso = discovery_date.date().isoformat()
    for peer_ticker, company in companies.items():
        if peer_ticker == ticker or company.get("sector") != sector:
            continue
        result = ticker_period_return(peer_ticker, discovery_iso, period_days)
        if result["return_percent"] is not None:
            returns.append(float(result["return_percent"]))
    if not returns:
        return None
    return sum(returns) / len(returns)


def validation_row(
    candidate: dict[str, Any],
    period_label: str,
    period_days: int,
    discovery_date: datetime,
    validation_date: datetime,
    benchmark_name: str | None,
    companies: dict[str, dict[str, Any]],
    sector_benchmarks: dict[str, str] | None = None,
) -> dict[str, Any]:
    ticker = str(candidate.get("ticker", "")).upper()
    company = companies.get(ticker, {})
    sector = candidate.get("sector") or company.get("sector")
    discovery_iso = discovery_date.date().isoformat()
    result = ticker_period_return(ticker, discovery_iso, period_days)
    benchmark_result = ticker_period_return(benchmark_name, discovery_iso, period_days) if benchmark_name else {}
    benchmark_return = benchmark_result.get("return_percent")
    benchmark_diff = None
    if result["return_percent"] is not None and benchmark_return is not None:
        benchmark_diff = float(result["return_percent"]) - float(benchmark_return)

    sector_average = sector_returns(ticker, sector, companies, discovery_date, period_days)
    sector_diff = None
    if result["return_percent"] is not None and sector_average is not None:
        sector_diff = float(result["return_percent"]) - sector_average

    # ピア平均は母数が少なくノイズが大きいため、セクターETFとの相対リターンも併記します。
    sector_etf = (sector_benchmarks or {}).get(str(sector)) if sector else None
    sector_etf_result = ticker_period_return(sector_etf, discovery_iso, period_days) if sector_etf else {}
    sector_etf_return = sector_etf_result.get("return_percent")
    sector_etf_diff = None
    if result["return_percent"] is not None and sector_etf_return is not None:
        sector_etf_diff = float(result["return_percent"]) - float(sector_etf_return)

    validation_result = classify_result(result["return_percent"], benchmark_diff, result["period_complete"], period_label)
    events = load_json(EVENT_DIR / f"{ticker}_events.json", [])
    evidence = sorted(set(candidate.get("evidence", [])) | {"Discovery", "Prices", "Events", "Knowledge"})
    return {
        "discovery_date": discovery_date.date().isoformat(),
        "validation_date": validation_date.date().isoformat(),
        "period": period_label,
        "ticker": ticker,
        "company": candidate.get("company") or company.get("company_name") or ticker,
        "sector": sector,
        "discovery_score": candidate.get("discovery_score"),
        "discovery_reasons": candidate.get("discovery_reasons", []),
        "start_date": result["start_date"],
        "end_date": result["end_date"],
        "start_price": result["start_price"],
        "end_price": result["end_price"],
        "return_percent": result["return_percent"],
        "benchmark": benchmark_name,
        "benchmark_return_percent": benchmark_return,
        "benchmark_diff_percent": benchmark_diff,
        "sector_average_return_percent": sector_average,
        "sector_diff_percent": sector_diff,
        "sector_benchmark": sector_etf,
        "sector_benchmark_return_percent": sector_etf_return,
        "sector_benchmark_diff_percent": sector_etf_diff,
        "validation_result": validation_result,
        "confidence": candidate.get("confidence"),
        "signal_strength": candidate.get("signal_strength"),
        "watch_points": candidate.get("watch_points", []),
        "evidence": evidence,
        "thresholds": threshold_note(period_label),
        "event_count": len(events) if isinstance(events, list) else None,
        "period_complete": result["period_complete"],
    }


def main() -> int:
    try:
        settings = load_yaml(SETTINGS_PATH)
    except Exception as error:
        print(f"settings.yaml 読み込みエラー: {error}")
        return 1

    logger = setup_logger(PROJECT_ROOT, settings, "compass.validation")
    timezone = get_timezone(settings)
    started_at = datetime.now(timezone)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    logger.info("Compass Research 04 - Backtesting & Validation Engine")
    logger.info("開始時刻: %s", started_at.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("保存先: %s", REPORT_DIR)

    snapshots = discovery_snapshots(timezone)
    if not snapshots:
        logger.warning("Discovery候補が見つかりません: %s / %s", DISCOVERY_PATH, DISCOVERY_MEMORY_DIR)
        return 0

    validation_date = datetime.now(timezone)
    benchmark_name, _ = load_benchmark()
    companies = companies_by_ticker()
    try:
        sector_benchmarks = load_sector_benchmarks(TICKERS_CONFIG_PATH)
    except Exception:
        sector_benchmarks = {}
    if sector_benchmarks:
        logger.info("セクターETF対応表: %s", sector_benchmarks)
    rows: list[dict[str, Any]] = []

    for discovery_date, candidates in snapshots:
        for candidate in candidates:
            for period_label, period_days in VALIDATION_PERIODS.items():
                try:
                    row = validation_row(
                        candidate=candidate,
                        period_label=period_label,
                        period_days=period_days,
                        discovery_date=discovery_date,
                        validation_date=validation_date,
                        benchmark_name=benchmark_name,
                        companies=companies,
                        sector_benchmarks=sector_benchmarks,
                    )
                    rows.append(row)
                    logger.info(
                        "[OK] %s %s %s: result=%s return=%s complete=%s",
                        row["discovery_date"],
                        row["ticker"],
                        period_label,
                        row["validation_result"],
                        row["return_percent"],
                        row["period_complete"],
                    )
                except Exception as error:
                    logger.exception("[NG] %s %s: エラー - %s", candidate.get("ticker"), period_label, error)

    history = save_history(REPORT_DIR, rows, persistent_rows=validation_memory_rows())
    history_rows = load_json(REPORT_DIR / "validation_history.json", [])
    summary = render_validation_summary(history_rows, validation_date.isoformat(), VALIDATION_PERIODS, benchmark_name)
    (REPORT_DIR / "validation_summary.md").write_text(summary, encoding="utf-8")

    finished_at = datetime.now(timezone)
    logger.info("Validation Summary保存: %s", REPORT_DIR / "validation_summary.md")
    logger.info("Validation History CSV保存: %s", REPORT_DIR / "validation_history.csv")
    logger.info("Validation History JSON保存: %s", REPORT_DIR / "validation_history.json")
    logger.info("終了時刻: %s", finished_at.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("処理結果: Discovery日 %s / 再評価 %s / 履歴合計 %s", len(snapshots), len(rows), len(history))
    return 0


if __name__ == "__main__":
    sys.exit(main())
