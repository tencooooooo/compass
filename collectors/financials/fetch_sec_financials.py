from __future__ import annotations

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]

from collectors.financials.cross_check import revenue_cross_check  # noqa: E402
from collectors.financials.sec_quarterly import extract_quarterly_financials  # noqa: E402
from collectors.sec.sec_client import SECClient  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.tickers import load_tickers  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "tickers.yaml"
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
FINANCIALS_DIR = PROJECT_ROOT / "storage" / "raw" / "financials"
CIK_CACHE_PATH = PROJECT_ROOT / "datasources" / "cache" / "sec" / "company_tickers.json"

# 成長率計算(最新四半期と前年同期)が成立する最低本数です。
MIN_QUARTERS_TO_ADOPT = 5


class SECFinancialsCollector:
    """SEC EDGARのXBRL companyfactsで、yfinance財務の四半期時系列を一次情報に置き換えます。"""

    def __init__(self, project_root: Path = PROJECT_ROOT, user_agent: str | None = None) -> None:
        self.project_root = project_root
        config = load_yaml(project_root / "config" / "datasources.yaml").get("datasources", {}).get("sec", {})
        configured_user_agent = user_agent or os.getenv(config.get("user_agent_env", "SEC_USER_AGENT"))
        self.client = SECClient(
            user_agent=configured_user_agent,
            request_interval=float(config.get("request_interval", 0.2)),
            max_retries=int(config.get("max_retries", 3)),
        )
        self.financials_dir = project_root / "storage" / "raw" / "financials"
        self.cache_path = project_root / "datasources" / "cache" / "sec" / "company_tickers.json"

    def enrich_ticker(self, ticker: str, fetched_at: str) -> tuple[bool, str]:
        cik, _company_name = self.client.ticker_to_cik(ticker, self.cache_path)
        company_facts = self.client.get_company_facts(cik)
        sec_rows = extract_quarterly_financials(company_facts)

        if len(sec_rows) < MIN_QUARTERS_TO_ADOPT:
            return False, f"{ticker}: SEC四半期データが{len(sec_rows)}本のため採用を見送り(yfinance系列を維持)"

        financials_path = self.financials_dir / f"{ticker}.json"
        financials: dict[str, Any] = {"ticker": ticker}
        if financials_path.exists():
            try:
                loaded = json.loads(financials_path.read_text(encoding="utf-8"))
                if isinstance(loaded, dict):
                    financials = loaded
            except (json.JSONDecodeError, OSError):
                pass

        # yfinance系列は比較・デバッグ用に別キーで保持し、分析はSEC系列を使います。
        previous_rows = financials.get("quarterly_financials")
        if isinstance(previous_rows, list) and financials.get("quarterly_source") != "sec_edgar":
            financials["quarterly_financials_yfinance"] = previous_rows

        financials["quarterly_financials"] = sec_rows
        financials["quarterly_source"] = "sec_edgar"
        financials["sec_cik"] = cik
        financials["sec_updated_at"] = fetched_at

        # 二重ソースを活かし、売上の乖離をデータ品質シグナルとして記録します。
        cross_check = revenue_cross_check(sec_rows, financials.get("quarterly_financials_yfinance"))
        financials["quarterly_cross_check"] = cross_check

        self.financials_dir.mkdir(parents=True, exist_ok=True)
        financials_path.write_text(json.dumps(financials, ensure_ascii=False, indent=2), encoding="utf-8")

        message = f"{ticker}: SEC四半期時系列 {len(sec_rows)}本で更新 -> {financials_path}"
        if cross_check["mismatches"]:
            quarters = ", ".join(item["fiscal_quarter"] for item in cross_check["mismatches"])
            message += f" | 要確認: yfinanceと売上乖離 {len(cross_check['mismatches'])}四半期 ({quarters})"
        return True, message

    def run(self, tickers: list[str], logger, fetched_at: str) -> int:
        updated: list[str] = []
        skipped: list[str] = []
        failed: list[str] = []
        for ticker in tickers:
            try:
                adopted, message = self.enrich_ticker(ticker, fetched_at)
                if adopted:
                    updated.append(ticker)
                    logger.info("[OK] %s", message)
                else:
                    skipped.append(ticker)
                    logger.warning("[SKIP] %s", message)
            except Exception as error:
                failed.append(ticker)
                logger.error("[NG] %s: エラー - %s", ticker, error)
        logger.info(
            "処理結果: 更新 %s / 見送り %s / 失敗 %s / 合計 %s",
            len(updated),
            len(skipped),
            len(failed),
            len(tickers),
        )
        return 1 if failed else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Enrich Compass financials with SEC EDGAR quarterly XBRL data.")
    parser.add_argument("--ticker", action="append", help="Ticker to enrich. Can be passed multiple times.")
    parser.add_argument("--user-agent", default=None, help="SEC User-Agent header. Defaults to SEC_USER_AGENT env var.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        settings = load_yaml(SETTINGS_PATH)
    except Exception as error:
        print(f"settings.yaml 読み込みエラー: {error}")
        return 1

    logger = setup_logger(PROJECT_ROOT, settings, "compass.sec_financials")
    timezone = get_timezone(settings)
    fetched_at = datetime.now(timezone).isoformat()

    tickers = args.ticker or load_tickers(CONFIG_PATH)
    logger.info("Compass - SEC quarterly financials enrichment")
    logger.info("対象銘柄: %s", ", ".join(tickers))

    collector = SECFinancialsCollector(user_agent=args.user_agent)
    return collector.run(tickers, logger, fetched_at)


if __name__ == "__main__":
    raise SystemExit(main())
