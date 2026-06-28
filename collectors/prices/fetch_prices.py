from datetime import datetime
import logging
from pathlib import Path
import sys

import pandas as pd
import yfinance as yf


# このファイル(collectors/prices/fetch_prices.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from collectors.base import BaseCollector  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.tickers import load_tickers  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "tickers.yaml"
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
CSV_COLUMNS = ["date", "open", "high", "low", "close", "volume"]


class PriceCollector(BaseCollector):
    """米国株の日足OHLCVを取得し、銘柄ごとにCSV保存するcollectorです。"""

    def __init__(self, project_root: Path, settings: dict, logger: logging.Logger):
        super().__init__(project_root, settings, logger)
        self.config_path = project_root / "config" / "tickers.yaml"
        self.output_dir = self.output_root / "raw" / "prices"
        self.period = settings.get("default_period", "5y")
        self.interval = settings.get("default_interval", "1d")

    def fetch_daily_prices(self, ticker: str) -> pd.DataFrame:
        """yfinanceから日足OHLCVを取得し、保存用の列名に整形します。"""
        raw = yf.download(
            ticker,
            period=self.period,
            interval=self.interval,
            auto_adjust=False,
            progress=False,
            threads=False,
        )

        if raw.empty:
            raise ValueError("取得結果が空でした。ティッカーや通信状況を確認してください。")

        # yfinanceのバージョンや指定方法によってはMultiIndex列になるため、単一階層に戻します。
        if isinstance(raw.columns, pd.MultiIndex):
            raw.columns = raw.columns.get_level_values(0)

        prices = raw.reset_index()
        prices = prices.rename(
            columns={
                "Date": "date",
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Close": "close",
                "Volume": "volume",
            }
        )

        missing_columns = [column for column in CSV_COLUMNS if column not in prices.columns]
        if missing_columns:
            raise ValueError(f"必要な列が見つかりません: {', '.join(missing_columns)}")

        prices = prices[CSV_COLUMNS].copy()
        prices["date"] = pd.to_datetime(prices["date"]).dt.strftime("%Y-%m-%d")

        return prices.dropna(subset=["date", "open", "high", "low", "close", "volume"])

    def merge_with_existing(self, new_data: pd.DataFrame, output_path: Path) -> pd.DataFrame:
        """既存CSVがある場合は結合し、date重複を除いて昇順に並べます。"""
        if output_path.exists():
            existing_data = pd.read_csv(output_path)
            combined = pd.concat([existing_data, new_data], ignore_index=True)
        else:
            combined = new_data

        combined = combined[CSV_COLUMNS].copy()
        combined["date"] = pd.to_datetime(combined["date"]).dt.strftime("%Y-%m-%d")
        combined = combined.drop_duplicates(subset=["date"], keep="last")
        combined = combined.sort_values("date").reset_index(drop=True)

        return combined

    def save_ticker_prices(self, ticker: str) -> tuple[bool, str]:
        """1銘柄分の取得からCSV保存までを実行します。"""
        output_path = self.output_dir / f"{ticker}.csv"

        try:
            new_data = self.fetch_daily_prices(ticker)
            merged_data = self.merge_with_existing(new_data, output_path)
            merged_data.to_csv(output_path, index=False)

            return True, (
                f"{ticker}: 保存完了 "
                f"({len(new_data)}件取得 / {len(merged_data)}件保存) -> {output_path}"
            )
        except Exception as error:
            return False, f"{ticker}: エラー - {error}"

    def run(self) -> int:
        timezone = get_timezone(self.settings)
        started_at = datetime.now(timezone)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.logger.info("Compass v1.0-alpha - Daily price fetch")
        self.logger.info("開始時刻: %s", started_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.logger.info("設定ファイル: %s", self.config_path)
        self.logger.info("保存先: %s", self.output_dir)
        self.logger.info("取得期間: %s", self.period)
        self.logger.info("取得間隔: %s", self.interval)

        try:
            tickers = load_tickers(self.config_path)
        except Exception as error:
            self.logger.exception("設定読み込みエラー: %s", error)
            return 1

        successful_tickers: list[str] = []
        failed_tickers: list[str] = []

        for ticker in tickers:
            ok, message = self.save_ticker_prices(ticker)
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

        # GitHub Actionsで失敗に気づきやすいよう、1銘柄でも失敗したら終了コード1にします。
        # ただし、処理自体は最後の銘柄まで継続します。
        return 1 if failed_tickers else 0


def main() -> int:
    try:
        settings = load_yaml(SETTINGS_PATH)
    except Exception as error:
        print(f"settings.yaml 読み込みエラー: {error}")
        return 1

    logger = setup_logger(PROJECT_ROOT, settings, "compass.prices")
    collector = PriceCollector(PROJECT_ROOT, settings, logger)
    return collector.run()


if __name__ == "__main__":
    sys.exit(main())
