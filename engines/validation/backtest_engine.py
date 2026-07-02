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
from engines.validation.validation_report import render_validation_summary  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.price_data import adjusted_close, normalize_price_frame  # noqa: E402


SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
DISCOVERY_PATH = PROJECT_ROOT / "reports" / "discovery" / "discovery_candidates.json"
REPORT_DIR = PROJECT_ROOT / "reports" / "validation"
PRICE_DIR = PROJECT_ROOT / "storage" / "raw" / "prices"
COMPANY_DIR = PROJECT_ROOT / "storage" / "raw" / "companies"
EVENT_DIR = PROJECT_ROOT / "storage" / "events"

VALIDATION_PERIODS = {
    "1w": 7,
    "1m": 30,
    "3m": 90,
    "6m": 180,
    "1y": 365,
}

VALIDATION_THRESHOLDS = {
    "1w": {"excellent": 3.0, "good": 1.5, "poor": -1.5, "benchmark_excellent": 2.0, "benchmark_good": 1.0, "benchmark_poor": -1.0},
    "1m": {"excellent": 6.0, "good": 3.0, "poor": -3.0, "benchmark_excellent": 4.0, "benchmark_good": 2.0, "benchmark_poor": -2.0},
    "3m": {"excellent": 10.0, "good": 5.0, "poor": -5.0, "benchmark_excellent": 7.0, "benchmark_good": 3.0, "benchmark_poor": -3.0},
    "6m": {"excellent": 13.0, "good": 7.0, "poor": -7.0, "benchmark_excellent": 9.0, "benchmark_good": 4.0, "benchmark_poor": -4.0},
    "1y": {"excellent": 15.0, "good": 8.0, "poor": -8.0, "benchmark_excellent": 10.0, "benchmark_good": 5.0, "benchmark_poor": -5.0},
}

BENCHMARK_CANDIDATES = ["SPY", "^GSPC"]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


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
    for peer_ticker, company in companies.items():
        if peer_ticker == ticker or company.get("sector") != sector:
            continue
        result = calculate_return(load_prices(peer_ticker), discovery_date, period_days)
        if result["return_percent"] is not None:
            returns.append(float(result["return_percent"]))
    if not returns:
        return None
    return sum(returns) / len(returns)


def threshold_note(period_label: str) -> str:
    threshold = VALIDATION_THRESHOLDS[period_label]
    return (
        "Validation thresholds "
        f"{period_label}: Excellent >= {threshold['excellent']}% or benchmark diff >= {threshold['benchmark_excellent']}%; "
        f"Good >= {threshold['good']}% or benchmark diff >= {threshold['benchmark_good']}%; "
        f"Poor <= {threshold['poor']}% or benchmark diff <= {threshold['benchmark_poor']}%."
    )


def classify_result(return_percent: float | None, benchmark_diff: float | None, period_complete: bool, period_label: str) -> str:
    if return_percent is None or not period_complete:
        return "Neutral"
    threshold = VALIDATION_THRESHOLDS[period_label]
    if return_percent >= threshold["excellent"] or (benchmark_diff is not None and benchmark_diff >= threshold["benchmark_excellent"]):
        return "Excellent"
    if return_percent >= threshold["good"] or (benchmark_diff is not None and benchmark_diff >= threshold["benchmark_good"]):
        return "Good"
    if return_percent <= threshold["poor"] or (benchmark_diff is not None and benchmark_diff <= threshold["benchmark_poor"]):
        return "Poor"
    return "Neutral"


def validation_row(
    candidate: dict[str, Any],
    period_label: str,
    period_days: int,
    discovery_date: datetime,
    validation_date: datetime,
    benchmark_name: str | None,
    benchmark_prices: pd.DataFrame,
    companies: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    ticker = str(candidate.get("ticker", "")).upper()
    company = companies.get(ticker, {})
    sector = candidate.get("sector") or company.get("sector")
    result = calculate_return(load_prices(ticker), discovery_date, period_days)
    benchmark_result = calculate_return(benchmark_prices, discovery_date, period_days) if benchmark_name else {}
    benchmark_return = benchmark_result.get("return_percent")
    benchmark_diff = None
    if result["return_percent"] is not None and benchmark_return is not None:
        benchmark_diff = float(result["return_percent"]) - float(benchmark_return)

    sector_average = sector_returns(ticker, sector, companies, discovery_date, period_days)
    sector_diff = None
    if result["return_percent"] is not None and sector_average is not None:
        sector_diff = float(result["return_percent"]) - sector_average

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
        "validation_result": validation_result,
        "confidence": candidate.get("confidence"),
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

    discovery = load_json(DISCOVERY_PATH, {})
    candidates = discovery.get("candidates", []) if isinstance(discovery, dict) else []
    if not candidates:
        logger.warning("Discovery候補が見つかりません: %s", DISCOVERY_PATH)
        return 0

    discovery_date = parse_datetime(discovery.get("generated_at"), timezone)
    validation_date = datetime.now(timezone)
    benchmark_name, benchmark_prices = load_benchmark()
    companies = companies_by_ticker()
    rows: list[dict[str, Any]] = []

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
                    benchmark_prices=benchmark_prices,
                    companies=companies,
                )
                rows.append(row)
                logger.info(
                    "[OK] %s %s: result=%s return=%s complete=%s",
                    row["ticker"],
                    period_label,
                    row["validation_result"],
                    row["return_percent"],
                    row["period_complete"],
                )
            except Exception as error:
                logger.exception("[NG] %s %s: エラー - %s", candidate.get("ticker"), period_label, error)

    history = save_history(REPORT_DIR, rows)
    summary = render_validation_summary(rows, validation_date.isoformat(), VALIDATION_PERIODS, benchmark_name)
    (REPORT_DIR / "validation_summary.md").write_text(summary, encoding="utf-8")

    finished_at = datetime.now(timezone)
    logger.info("Validation Summary保存: %s", REPORT_DIR / "validation_summary.md")
    logger.info("Validation History CSV保存: %s", REPORT_DIR / "validation_history.csv")
    logger.info("Validation History JSON保存: %s", REPORT_DIR / "validation_history.json")
    logger.info("終了時刻: %s", finished_at.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("処理結果: 新規 %s / 履歴合計 %s", len(rows), len(history))
    return 0


if __name__ == "__main__":
    sys.exit(main())
