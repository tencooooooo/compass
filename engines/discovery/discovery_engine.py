from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Any

import pandas as pd


# このファイル(engines/discovery/discovery_engine.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]

from engines.discovery.candidate_selector import build_candidate, select_candidates  # noqa: E402
from engines.discovery.discovery_report import render_candidate_detail, render_candidates_report  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.price_data import normalize_price_frame  # noqa: E402
from utils.tickers import load_tickers  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "tickers.yaml"
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
REPORT_DIR = PROJECT_ROOT / "reports" / "discovery"
DETAIL_DIR = REPORT_DIR / "candidate_details"
SCORING_JSON_PATH = PROJECT_ROOT / "reports" / "scoring" / "company_scores.json"
MARKET_DASHBOARD_PATH = PROJECT_ROOT / "reports" / "market" / "market_dashboard.json"


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def load_prices(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    prices = pd.read_csv(path)
    if prices.empty or "date" not in prices.columns:
        return pd.DataFrame()
    return normalize_price_frame(prices)


def scoring_by_ticker() -> dict[str, dict[str, Any]]:
    scoring = load_json(SCORING_JSON_PATH, {})
    results = scoring.get("results", []) if isinstance(scoring, dict) else []
    return {str(item.get("ticker")).upper(): item for item in results if item.get("ticker")}


def main() -> int:
    try:
        settings = load_yaml(SETTINGS_PATH)
    except Exception as error:
        print(f"settings.yaml 読み込みエラー: {error}")
        return 1

    logger = setup_logger(PROJECT_ROOT, settings, "compass.discovery")
    timezone = get_timezone(settings)
    started_at = datetime.now(timezone)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    DETAIL_DIR.mkdir(parents=True, exist_ok=True)

    logger.info("Compass Research 03 - Discovery Engine")
    logger.info("開始時刻: %s", started_at.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("保存先: %s", REPORT_DIR)

    try:
        tickers = load_tickers(CONFIG_PATH)
    except Exception as error:
        logger.exception("設定読み込みエラー: %s", error)
        return 1

    scores = scoring_by_ticker()
    market_dashboard = load_json(MARKET_DASHBOARD_PATH, {})
    candidates: list[dict[str, Any]] = []
    failed_tickers: list[str] = []

    for ticker in tickers:
        try:
            company = load_json(PROJECT_ROOT / "storage" / "raw" / "companies" / f"{ticker}.json", {})
            financials = load_json(PROJECT_ROOT / "storage" / "raw" / "financials" / f"{ticker}.json", {})
            news_items = load_json(PROJECT_ROOT / "storage" / "raw" / "news" / f"{ticker}.json", [])
            events = load_json(PROJECT_ROOT / "storage" / "events" / f"{ticker}_events.json", [])
            prices = load_prices(PROJECT_ROOT / "storage" / "raw" / "prices" / f"{ticker}.csv")
            company_report = load_text(PROJECT_ROOT / "reports" / "company_analysis" / f"{ticker}.md")
            candidate = build_candidate(
                ticker=ticker,
                company=company,
                financials=financials,
                news_items=news_items if isinstance(news_items, list) else [],
                events=events if isinstance(events, list) else [],
                prices=prices,
                score_result=scores.get(ticker, {}),
                company_report=company_report,
                market_dashboard=market_dashboard,
            )
            candidates.append(candidate)
            logger.info("[OK] %s: discovery_score=%s status=%s", ticker, candidate["discovery_score"], candidate["status"])
        except Exception as error:
            failed_tickers.append(ticker)
            logger.exception("[NG] %s: エラー - %s", ticker, error)

    selected = select_candidates(candidates)
    generated_at = datetime.now(timezone).isoformat()
    output = {
        "project": settings.get("project_name", "Compass"),
        "engine": "Discovery Engine",
        "version": settings.get("project_version", "v1.0-alpha"),
        "generated_at": generated_at,
        "universe": {
            "source": "config/tickers.yaml",
            "count": len(tickers),
            "tickers": tickers,
        },
        "market": market_dashboard.get("market", {}),
        "candidates": selected,
        "all_companies": candidates,
    }

    (REPORT_DIR / "discovery_candidates.json").write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    report = render_candidates_report(selected, market_dashboard.get("market", {}))
    (REPORT_DIR / "discovery_candidates.md").write_text(report, encoding="utf-8")
    for candidate in selected:
        (DETAIL_DIR / f"{candidate['ticker']}.md").write_text(render_candidate_detail(candidate), encoding="utf-8")

    finished_at = datetime.now(timezone)
    logger.info("候補レポート保存: %s", REPORT_DIR / "discovery_candidates.md")
    logger.info("候補JSON保存: %s", REPORT_DIR / "discovery_candidates.json")
    logger.info("終了時刻: %s", finished_at.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("処理結果: 候補 %s / 対象 %s / 失敗 %s", len(selected), len(candidates), len(failed_tickers))
    return 1 if failed_tickers else 0


if __name__ == "__main__":
    sys.exit(main())
