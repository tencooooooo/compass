from datetime import datetime
import json
import math
from numbers import Integral, Real
from pathlib import Path
import sys
from typing import Any

import yfinance as yf


# このファイル(collectors/companies/fetch_company_profiles.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]

from collectors.base import BaseCollector  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.tickers import load_tickers  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "tickers.yaml"
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"

PROFILE_FIELDS = {
    "ticker": None,
    "company_name": "longName",
    "sector": "sector",
    "industry": "industry",
    "country": "country",
    "currency": "currency",
    "exchange": "exchange",
    "market_cap": "marketCap",
    "enterprise_value": "enterpriseValue",
    "shares_outstanding": "sharesOutstanding",
    "beta": "beta",
    "trailing_pe": "trailingPE",
    "forward_pe": "forwardPE",
    "peg_ratio": "pegRatio",
    "price_to_book": "priceToBook",
    "eps": "trailingEps",
    "forward_eps": "forwardEps",
    "dividend_yield": "dividendYield",
    "52_week_high": "fiftyTwoWeekHigh",
    "52_week_low": "fiftyTwoWeekLow",
    "average_volume": "averageVolume",
    "employees": "fullTimeEmployees",
    "website": "website",
    "business_summary": "longBusinessSummary",
}


def normalize_value(value: Any) -> Any:
    """JSON保存しやすいように、取得値を基本的な型へ揃えます。"""
    if value in ("", "None", "N/A"):
        return None
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        number = float(value)
        return None if not math.isfinite(number) else number
    return str(value)


class CompanyProfileCollector(BaseCollector):
    """yfinanceから企業プロフィールを取得し、銘柄ごとにJSON保存するcollectorです。"""

    def __init__(self, project_root: Path, settings: dict, logger):
        super().__init__(project_root, settings, logger)
        self.config_path = project_root / "config" / "tickers.yaml"
        self.output_dir = self.output_root / "raw" / "companies"

    def fetch_company_profile(self, ticker: str) -> dict[str, Any]:
        """yfinanceのinfoから、AI分析の基礎になる企業情報を抽出します。"""
        info = yf.Ticker(ticker).info or {}

        if not info:
            raise ValueError("企業情報の取得結果が空でした。")

        profile: dict[str, Any] = {}
        for output_key, source_key in PROFILE_FIELDS.items():
            if output_key == "ticker":
                profile[output_key] = ticker
            else:
                profile[output_key] = normalize_value(info.get(source_key))

        return profile

    def save_company_profile(self, ticker: str) -> tuple[bool, str]:
        """1銘柄分の企業情報を取得し、JSONへ上書き保存します。"""
        output_path = self.output_dir / f"{ticker}.json"

        try:
            profile = self.fetch_company_profile(ticker)
            with output_path.open("w", encoding="utf-8") as file:
                json.dump(profile, file, ensure_ascii=False, indent=2)

            return True, f"{ticker}: 保存完了 -> {output_path}"
        except Exception as error:
            return False, f"{ticker}: エラー - {error}"

    def run(self) -> int:
        timezone = get_timezone(self.settings)
        started_at = datetime.now(timezone)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.logger.info("Compass v1.0-alpha - Company profile fetch")
        self.logger.info("開始時刻: %s", started_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.logger.info("設定ファイル: %s", self.config_path)
        self.logger.info("保存先: %s", self.output_dir)

        try:
            tickers = load_tickers(self.config_path)
        except Exception as error:
            self.logger.exception("設定読み込みエラー: %s", error)
            return 1

        successful_tickers: list[str] = []
        failed_tickers: list[str] = []

        for ticker in tickers:
            ok, message = self.save_company_profile(ticker)
            if ok:
                successful_tickers.append(ticker)
                self.logger.info("[OK] %s", message)
            else:
                failed_tickers.append(ticker)
                self.logger.error("[NG] %s", message)

        finished_at = datetime.now(timezone)
        self.logger.info("終了時刻: %s", finished_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.logger.info("取得成功銘柄: %s", ", ".join(successful_tickers) or "なし")
        self.logger.info("失敗銘柄: %s", ", ".join(failed_tickers) or "なし")
        self.logger.info(
            "処理結果: 成功 %s / 失敗 %s / 合計 %s",
            len(successful_tickers),
            len(failed_tickers),
            len(tickers),
        )

        return 1 if failed_tickers else 0


def main() -> int:
    try:
        settings = load_yaml(SETTINGS_PATH)
    except Exception as error:
        print(f"settings.yaml 読み込みエラー: {error}")
        return 1

    logger = setup_logger(PROJECT_ROOT, settings, "compass.companies")
    collector = CompanyProfileCollector(PROJECT_ROOT, settings, logger)
    return collector.run()


if __name__ == "__main__":
    sys.exit(main())
