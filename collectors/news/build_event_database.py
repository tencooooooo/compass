from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

import pandas as pd


# このファイル(collectors/news/build_event_database.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]

from collectors.base import BaseCollector  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.price_data import adjusted_close, normalize_price_frame  # noqa: E402
from utils.tickers import load_tickers  # noqa: E402
from utils.values import safe_float  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "tickers.yaml"
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"


def make_event_id(ticker: str, published_at: Any, title: Any, url: Any) -> str:
    """ニュース内容から安定したevent_idを作ります。"""
    raw = f"{ticker}|{published_at or ''}|{title or ''}|{url or ''}"
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]
    return f"{ticker}_{digest}"


MARKET_TIMEZONE = "America/New_York"
MARKET_CLOSE_HOUR = 16


def parse_news_date(published_at: Any) -> pd.Timestamp | None:
    """published_atから、株価反応を観測すべき取引日を求めます。

    米国市場の引け(16:00 ET)以降に出たニュースの反応は翌営業日に現れるため、
    ET基準で16時以降は翌日に帰属させます。
    """
    if not published_at:
        return None
    try:
        parsed = pd.to_datetime(published_at, utc=True)
        if pd.isna(parsed):
            return None
        eastern = parsed.tz_convert(MARKET_TIMEZONE)
        if eastern.hour >= MARKET_CLOSE_HOUR:
            eastern = eastern + pd.Timedelta(days=1)
        return eastern.tz_localize(None).normalize()
    except Exception:
        return None


def load_prices(price_path: Path) -> pd.DataFrame:
    """価格CSVを読み込み、日付昇順に整えます。"""
    if not price_path.exists():
        return pd.DataFrame()

    prices = pd.read_csv(price_path)
    if prices.empty or "date" not in prices.columns:
        return pd.DataFrame()

    return normalize_price_frame(prices)


def find_price_row(prices: pd.DataFrame, news_date: pd.Timestamp | None) -> tuple[Any, Any]:
    """ニュース日以降の最初の取引日と、その前営業日の行を返します。"""
    if prices.empty or news_date is None:
        return None, None

    matches = prices.index[prices["date"] >= news_date].tolist()
    if not matches:
        return None, None

    current_index = matches[0]
    previous_index = current_index - 1
    current_row = prices.loc[current_index]
    previous_row = prices.loc[previous_index] if previous_index >= 0 else None

    return current_row, previous_row


def build_event(ticker: str, news_item: dict[str, Any], prices: pd.DataFrame) -> dict[str, Any]:
    """ニュース1件と価格CSVから、イベントレコードを作ります。"""
    news_date = parse_news_date(news_item.get("published_at"))
    current_row, previous_row = find_price_row(prices, news_date)

    close_price = adjusted_close(current_row) if current_row is not None else None
    previous_close = adjusted_close(previous_row) if previous_row is not None else None
    volume = safe_float(current_row["volume"]) if current_row is not None else None

    price_change_percent = None
    if close_price is not None and previous_close not in (None, 0):
        price_change_percent = ((close_price - previous_close) / previous_close) * 100

    return {
        "event_id": make_event_id(
            ticker,
            news_item.get("published_at"),
            news_item.get("title"),
            news_item.get("url"),
        ),
        "ticker": ticker,
        "published_at": news_item.get("published_at"),
        "title": news_item.get("title"),
        "url": news_item.get("url"),
        "source": news_item.get("source"),
        "close_price": close_price,
        "previous_close": previous_close,
        "price_change_percent": price_change_percent,
        "volume": volume,
    }


class EventDatabaseBuilder(BaseCollector):
    """保存済みニュースと価格CSVからイベントDBを作成します。"""

    def __init__(self, project_root: Path, settings: dict, logger):
        super().__init__(project_root, settings, logger)
        self.config_path = project_root / "config" / "tickers.yaml"
        self.news_dir = self.output_root / "raw" / "news"
        self.prices_dir = self.output_root / "raw" / "prices"
        self.output_dir = self.output_root / "events"

    def build_ticker_events(self, ticker: str) -> tuple[bool, str]:
        """1銘柄分のイベントDBを作成します。"""
        news_path = self.news_dir / f"{ticker}.json"
        price_path = self.prices_dir / f"{ticker}.csv"
        output_path = self.output_dir / f"{ticker}_events.json"

        try:
            if not news_path.exists():
                raise FileNotFoundError(f"ニュースJSONが見つかりません: {news_path}")

            news_items = json.loads(news_path.read_text(encoding="utf-8"))
            if not isinstance(news_items, list):
                raise ValueError(f"ニュースJSONの形式がlistではありません: {news_path}")

            prices = load_prices(price_path)
            events = [
                build_event(ticker, news_item, prices)
                for news_item in news_items
                if isinstance(news_item, dict)
            ]

            with output_path.open("w", encoding="utf-8") as file:
                json.dump(events, file, ensure_ascii=False, indent=2)

            return True, f"{ticker}: 保存完了 ({len(events)}件) -> {output_path}"
        except Exception as error:
            return False, f"{ticker}: エラー - {error}"

    def run(self) -> int:
        timezone_setting = get_timezone(self.settings)
        started_at = datetime.now(timezone_setting)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.logger.info("Compass v1.0-alpha - Event database build")
        self.logger.info("開始時刻: %s", started_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.logger.info("ニュース保存先: %s", self.news_dir)
        self.logger.info("価格保存先: %s", self.prices_dir)
        self.logger.info("イベント保存先: %s", self.output_dir)

        try:
            tickers = load_tickers(self.config_path)
        except Exception as error:
            self.logger.exception("設定読み込みエラー: %s", error)
            return 1

        successful_tickers: list[str] = []
        failed_tickers: list[str] = []

        for ticker in tickers:
            ok, message = self.build_ticker_events(ticker)
            if ok:
                successful_tickers.append(ticker)
                self.logger.info("[OK] %s", message)
            else:
                failed_tickers.append(ticker)
                self.logger.error("[NG] %s", message)

        finished_at = datetime.now(timezone_setting)
        self.logger.info("終了時刻: %s", finished_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.logger.info("作成成功銘柄: %s", ", ".join(successful_tickers) or "なし")
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

    logger = setup_logger(PROJECT_ROOT, settings, "compass.events")
    builder = EventDatabaseBuilder(PROJECT_ROOT, settings, logger)
    return builder.run()


if __name__ == "__main__":
    sys.exit(main())
