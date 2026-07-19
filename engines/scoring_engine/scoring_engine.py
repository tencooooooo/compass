from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Any

import pandas as pd


# このファイル(engines/scoring_engine/scoring_engine.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]

from engines.scoring_engine.score_calculator import calculate_company_score  # noqa: E402
from engines.scoring_engine.score_explainer import render_explanation  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.price_data import normalize_price_frame  # noqa: E402
from utils.tickers import load_tickers  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "tickers.yaml"
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
PROMPT_PATH = PROJECT_ROOT / "prompts" / "scoring_engine_prompt.md"
REPORT_DIR = PROJECT_ROOT / "reports" / "scoring"
EXPLANATION_DIR = REPORT_DIR / "explanations"

# Momentumの相対評価に使う市場ベンチマーク。validation の backtest_engine と同じ優先順です。
BENCHMARK_CANDIDATES = ["SPY", "^GSPC"]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_prices(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    prices = pd.read_csv(path)
    if prices.empty or "date" not in prices.columns:
        return pd.DataFrame()
    return normalize_price_frame(prices)


def load_ticker_inputs(ticker: str) -> dict[str, Any]:
    return {
        "company": load_json(PROJECT_ROOT / "storage" / "raw" / "companies" / f"{ticker}.json", {}),
        "financials": load_json(PROJECT_ROOT / "storage" / "raw" / "financials" / f"{ticker}.json", {}),
        "news": load_json(PROJECT_ROOT / "storage" / "raw" / "news" / f"{ticker}.json", []),
        "events": load_json(PROJECT_ROOT / "storage" / "events" / f"{ticker}_events.json", []),
        "prices": load_prices(PROJECT_ROOT / "storage" / "raw" / "prices" / f"{ticker}.csv"),
    }


def load_benchmark_prices() -> tuple[str | None, pd.DataFrame]:
    for ticker in BENCHMARK_CANDIDATES:
        prices = load_prices(PROJECT_ROOT / "storage" / "raw" / "prices" / f"{ticker}.csv")
        if not prices.empty:
            return ticker, prices
    return None, pd.DataFrame()


def load_company_profile_pool() -> list[dict[str, Any]]:
    """保存済みの全企業プロファイル(監視銘柄+ピア銘柄)をセクター相対評価の母集団として読み込みます。"""
    pool: list[dict[str, Any]] = []
    company_dir = PROJECT_ROOT / "storage" / "raw" / "companies"
    if not company_dir.exists():
        return pool
    for path in sorted(company_dir.glob("*.json")):
        data = load_json(path, {})
        if isinstance(data, dict) and data.get("sector"):
            pool.append(data)
    return pool


def sector_companies_for(
    ticker: str,
    inputs_by_ticker: dict[str, dict[str, Any]],
    profile_pool: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    company = inputs_by_ticker.get(ticker, {}).get("company", {})
    sector = company.get("sector")
    if not sector:
        return []
    return [peer for peer in profile_pool if peer.get("sector") == sector]


def csv_row(score_result: dict[str, Any]) -> dict[str, Any]:
    scores = score_result["scores"]
    return {
        "ticker": score_result["ticker"],
        "company_name": score_result.get("company_name"),
        "total_score": score_result["total_score"],
        "growth_score": scores["Growth"]["score"],
        "financial_health_score": scores["Financial Health"]["score"],
        "valuation_score": scores["Valuation"]["score"],
        "momentum_score": scores["Momentum"]["score"],
        "news_score": scores["News"]["score"],
        "confidence": score_result["confidence"]["level"],
        "confidence_completeness": score_result["confidence"]["completeness_score"],
        "evidence_sources": ", ".join(score_result["evidence_sources"]),
    }


def main() -> int:
    try:
        settings = load_yaml(SETTINGS_PATH)
    except Exception as error:
        print(f"settings.yaml 読み込みエラー: {error}")
        return 1

    logger = setup_logger(PROJECT_ROOT, settings, "compass.scoring_engine")
    timezone = get_timezone(settings)
    started_at = datetime.now(timezone)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    EXPLANATION_DIR.mkdir(parents=True, exist_ok=True)

    logger.info("Compass Research 01 - Explainable Scoring Engine")
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

    results: list[dict[str, Any]] = []
    successful_tickers: list[str] = []
    failed_tickers: list[str] = []
    inputs_by_ticker = {ticker: load_ticker_inputs(ticker) for ticker in tickers}
    profile_pool = load_company_profile_pool()
    logger.info("セクター相対評価の母集団: %s 社(ピア銘柄を含む)", len(profile_pool))
    benchmark_name, benchmark_prices = load_benchmark_prices()
    if benchmark_name:
        logger.info("Momentumベンチマーク: %s", benchmark_name)
    else:
        logger.warning("ベンチマーク価格が見つからないため、Momentumは絶対リターンで評価します。")

    for ticker in tickers:
        try:
            inputs = inputs_by_ticker[ticker]
            score_result = calculate_company_score(
                ticker=ticker,
                company=inputs["company"],
                financials=inputs["financials"],
                news_items=inputs["news"] if isinstance(inputs["news"], list) else [],
                events=inputs["events"] if isinstance(inputs["events"], list) else [],
                prices=inputs["prices"],
                sector_companies=sector_companies_for(ticker, inputs_by_ticker, profile_pool),
                benchmark_prices=benchmark_prices,
                benchmark_name=benchmark_name,
            )
            results.append(score_result)
            explanation = render_explanation(score_result)
            (EXPLANATION_DIR / f"{ticker}.md").write_text(explanation, encoding="utf-8")
            successful_tickers.append(ticker)
            logger.info("[OK] %s: score=%s confidence=%s", ticker, score_result["total_score"], score_result["confidence"]["level"])
        except Exception as error:
            failed_tickers.append(ticker)
            logger.exception("[NG] %s: エラー - %s", ticker, error)

    generated_at = datetime.now(timezone).isoformat()
    output = {
        "project": settings.get("project_name", "Compass"),
        "engine": "Explainable Scoring Engine",
        "version": settings.get("project_version", "v1.0-alpha"),
        "generated_at": generated_at,
        "max_score": 100,
        "category_max_score": 20,
        "results": results,
    }

    json_path = REPORT_DIR / "company_scores.json"
    json_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    csv_path = REPORT_DIR / "company_scores.csv"
    pd.DataFrame([csv_row(result) for result in results]).to_csv(csv_path, index=False, encoding="utf-8")

    finished_at = datetime.now(timezone)
    logger.info("CSV保存: %s", csv_path)
    logger.info("JSON保存: %s", json_path)
    logger.info("終了時刻: %s", finished_at.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("生成成功銘柄: %s", ", ".join(successful_tickers) or "なし")
    logger.info("失敗銘柄: %s", ", ".join(failed_tickers) or "なし")
    logger.info("処理結果: 成功 %s / 失敗 %s / 合計 %s", len(successful_tickers), len(failed_tickers), len(tickers))

    return 1 if failed_tickers else 0


if __name__ == "__main__":
    sys.exit(main())
