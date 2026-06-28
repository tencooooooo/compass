from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Any

import pandas as pd


# このファイル(engines/market_intelligence/market_monitor.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from engines.market_intelligence.market_summary import render_market_psychology, render_market_summary, render_sector_summary  # noqa: E402
from engines.market_intelligence.sector_analysis import average, build_sector_summaries, calculate_ticker_momentum, safe_float  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.tickers import load_tickers  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "tickers.yaml"
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
PROMPT_PATH = PROJECT_ROOT / "prompts" / "market_intelligence_prompt.md"
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"
REPORT_DIR = PROJECT_ROOT / "reports" / "market"
SCORING_CSV_PATH = PROJECT_ROOT / "reports" / "scoring" / "company_scores.csv"
COMPARATIVE_REPORT_DIR = PROJECT_ROOT / "reports" / "comparative_analysis"


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
    prices = prices.copy()
    prices["date"] = pd.to_datetime(prices["date"])
    return prices.sort_values("date").reset_index(drop=True)


def load_scoring_rows() -> dict[str, dict[str, Any]]:
    if not SCORING_CSV_PATH.exists():
        return {}
    scores = pd.read_csv(SCORING_CSV_PATH)
    if scores.empty or "ticker" not in scores.columns:
        return {}
    return {str(row["ticker"]).upper(): row.to_dict() for _, row in scores.iterrows()}


def build_ticker_rows(tickers: list[str]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    scoring_rows = load_scoring_rows()
    ticker_rows: list[dict[str, Any]] = []
    all_news: list[dict[str, Any]] = []
    all_events: list[dict[str, Any]] = []

    for ticker in tickers:
        company = load_json(PROJECT_ROOT / "storage" / "raw" / "companies" / f"{ticker}.json", {})
        financials = load_json(PROJECT_ROOT / "storage" / "raw" / "financials" / f"{ticker}.json", {})
        news_items = load_json(PROJECT_ROOT / "storage" / "raw" / "news" / f"{ticker}.json", [])
        events = load_json(PROJECT_ROOT / "storage" / "events" / f"{ticker}_events.json", [])
        prices = load_prices(PROJECT_ROOT / "storage" / "raw" / "prices" / f"{ticker}.csv")
        momentum = calculate_ticker_momentum(prices)
        score = scoring_rows.get(ticker, {})

        if isinstance(news_items, list):
            for item in news_items:
                if isinstance(item, dict):
                    all_news.append({**item, "ticker": ticker})
        if isinstance(events, list):
            for event in events:
                if isinstance(event, dict):
                    all_events.append({**event, "ticker": ticker})

        ticker_rows.append(
            {
                "ticker": ticker,
                "company_name": company.get("company_name"),
                "sector": company.get("sector") or "Unknown",
                "industry": company.get("industry"),
                "trailing_pe": company.get("trailing_pe"),
                "eps": company.get("eps") if company.get("eps") is not None else financials.get("eps"),
                "total_score": score.get("total_score"),
                "financial_health_score": score.get("financial_health_score"),
                "momentum_1m": momentum["1m"],
                "momentum_3m": momentum["3m"],
                "momentum_6m": momentum["6m"],
                "momentum_1y": momentum["1y"],
                "news_count": len(news_items) if isinstance(news_items, list) else 0,
                "event_count": len(events) if isinstance(events, list) else 0,
            }
        )
    return ticker_rows, all_news, all_events


def top_news(news_items: list[dict[str, Any]], limit: int = 5) -> list[dict[str, Any]]:
    return sorted(news_items, key=lambda item: str(item.get("published_at") or ""), reverse=True)[:limit]


def top_events(events: list[dict[str, Any]], limit: int = 5) -> list[dict[str, Any]]:
    def event_score(event: dict[str, Any]) -> tuple[int, float, str]:
        reaction = safe_float(event.get("price_change_percent"))
        if reaction is not None:
            return (1, abs(reaction), str(event.get("published_at") or ""))
        return (0, 0, str(event.get("published_at") or ""))

    return sorted(events, key=event_score, reverse=True)[:limit]


def comparative_report_names() -> list[str]:
    if not COMPARATIVE_REPORT_DIR.exists():
        return []
    return [path.name for path in sorted(COMPARATIVE_REPORT_DIR.glob("*.md"))]


def market_snapshot(ticker_rows: list[dict[str, Any]], sector_summaries: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "ticker_count": len(ticker_rows),
        "sector_count": len(sector_summaries),
        "average_momentum_1m": average([row.get("momentum_1m") for row in ticker_rows]),
        "average_momentum_3m": average([row.get("momentum_3m") for row in ticker_rows]),
        "average_momentum_6m": average([row.get("momentum_6m") for row in ticker_rows]),
        "average_momentum_1y": average([row.get("momentum_1y") for row in ticker_rows]),
        "average_score": average([row.get("total_score") for row in ticker_rows]),
        "news_count": sum(int(row.get("news_count") or 0) for row in ticker_rows),
        "event_count": sum(int(row.get("event_count") or 0) for row in ticker_rows),
    }


def dashboard_payload(
    market: dict[str, Any],
    sectors: list[dict[str, Any]],
    events: list[dict[str, Any]],
    psychology: str,
    generated_at: str,
) -> dict[str, Any]:
    return {
        "market": market,
        "sectors": sectors,
        "top_events": events,
        "summary": {
            "generated_at": generated_at,
            "engine": "Market Intelligence Engine",
            "market_psychology": psychology,
        },
    }


def main() -> int:
    try:
        settings = load_yaml(SETTINGS_PATH)
    except Exception as error:
        print(f"settings.yaml 読み込みエラー: {error}")
        return 1

    logger = setup_logger(PROJECT_ROOT, settings, "compass.market_intelligence")
    timezone = get_timezone(settings)
    started_at = datetime.now(timezone)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    logger.info("Compass Research 02 - Market Intelligence Engine")
    logger.info("開始時刻: %s", started_at.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("保存先: %s", REPORT_DIR)

    try:
        tickers = load_tickers(CONFIG_PATH)
    except Exception as error:
        logger.exception("設定読み込みエラー: %s", error)
        return 1

    if PROMPT_PATH.exists():
        logger.info("プロンプト: %s", PROMPT_PATH)
    else:
        logger.warning("プロンプトが見つかりません: %s", PROMPT_PATH)

    ticker_rows, news_items, events = build_ticker_rows(tickers)
    sector_summaries = build_sector_summaries(ticker_rows)
    market = market_snapshot(ticker_rows, sector_summaries)
    recent_news = top_news(news_items)
    important_events = top_events(events)
    psychology_knowledge = load_text(KNOWLEDGE_DIR / "market_psychology.md")
    psychology = render_market_psychology(market, sector_summaries, psychology_knowledge[:900])
    comparative_reports = comparative_report_names()
    generated_at = datetime.now(timezone).isoformat()

    market_report = render_market_summary(market, sector_summaries, recent_news, important_events, psychology, comparative_reports)
    sector_report = render_sector_summary(sector_summaries, ticker_rows)
    dashboard = dashboard_payload(market, sector_summaries, important_events, psychology, generated_at)

    (REPORT_DIR / "market_summary.md").write_text(market_report, encoding="utf-8")
    (REPORT_DIR / "sector_summary.md").write_text(sector_report, encoding="utf-8")
    (REPORT_DIR / "market_dashboard.json").write_text(json.dumps(dashboard, ensure_ascii=False, indent=2), encoding="utf-8")

    finished_at = datetime.now(timezone)
    logger.info("市場レポート保存: %s", REPORT_DIR / "market_summary.md")
    logger.info("セクターレポート保存: %s", REPORT_DIR / "sector_summary.md")
    logger.info("Dashboard JSON保存: %s", REPORT_DIR / "market_dashboard.json")
    logger.info("終了時刻: %s", finished_at.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("処理結果: 対象銘柄 %s / セクター %s / ニュース %s / イベント %s", len(ticker_rows), len(sector_summaries), len(news_items), len(events))

    return 0


if __name__ == "__main__":
    sys.exit(main())
