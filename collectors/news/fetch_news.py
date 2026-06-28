from datetime import datetime, timezone
import json
from pathlib import Path
import sys
from typing import Any

import pandas as pd
import yfinance as yf


# このファイル(collectors/news/fetch_news.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from collectors.base import BaseCollector  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.tickers import load_tickers  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "tickers.yaml"
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
MAX_NEWS_ITEMS = 20


def normalize_value(value: Any) -> Any:
    """JSON保存しやすい基本型へ揃えます。"""
    if value in ("", "None", "N/A"):
        return None
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, pd.Timestamp):
        return value.isoformat()
    return str(value)


def parse_datetime(value: Any) -> str | None:
    """yfinanceのニュース日時をISO形式へ変換します。"""
    if value in (None, ""):
        return None

    try:
        if isinstance(value, (int, float)):
            return datetime.fromtimestamp(value, tz=timezone.utc).isoformat()
        parsed = pd.to_datetime(value, utc=True)
        if pd.isna(parsed):
            return None
        return parsed.isoformat()
    except Exception:
        return None


def nested_get(data: dict[str, Any], path: list[str]) -> Any:
    """ネストしたdictから値を取り出します。存在しない場合はNoneです。"""
    current: Any = data
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def extract_url(news_item: dict[str, Any], content: dict[str, Any]) -> Any:
    """yfinanceの複数形式に対応してニュースURLを取り出します。"""
    return (
        news_item.get("link")
        or nested_get(content, ["canonicalUrl", "url"])
        or nested_get(content, ["clickThroughUrl", "url"])
        or content.get("url")
    )


def normalize_news_item(ticker: str, news_item: dict[str, Any]) -> dict[str, Any]:
    """yfinanceのニュース1件を、このプロジェクトの保存形式へ変換します。"""
    content = news_item.get("content") if isinstance(news_item.get("content"), dict) else {}
    provider = content.get("provider") if isinstance(content.get("provider"), dict) else {}

    related_tickers = (
        news_item.get("relatedTickers")
        or content.get("relatedTickers")
        or nested_get(content, ["finance", "relatedTickers"])
    )
    if not isinstance(related_tickers, list):
        related_tickers = None

    return {
        "ticker": ticker,
        "title": normalize_value(news_item.get("title") or content.get("title")),
        "summary": normalize_value(
            news_item.get("summary")
            or content.get("summary")
            or content.get("description")
        ),
        "published_at": parse_datetime(
            news_item.get("providerPublishTime")
            or content.get("pubDate")
            or content.get("displayTime")
        ),
        "publisher": normalize_value(
            news_item.get("publisher")
            or provider.get("displayName")
            or provider.get("name")
        ),
        "url": normalize_value(extract_url(news_item, content)),
        "language": normalize_value(
            news_item.get("language")
            or content.get("language")
        ),
        "source": normalize_value(
            news_item.get("type")
            or content.get("contentType")
            or news_item.get("source")
        ),
        "related_tickers": related_tickers,
    }


class NewsCollector(BaseCollector):
    """yfinanceからニュースを取得し、銘柄ごとにJSON保存するcollectorです。"""

    def __init__(self, project_root: Path, settings: dict, logger):
        super().__init__(project_root, settings, logger)
        self.config_path = project_root / "config" / "tickers.yaml"
        self.output_dir = self.output_root / "raw" / "news"

    def fetch_news(self, ticker: str) -> list[dict[str, Any]]:
        """1銘柄あたり最大20件のニュースを取得します。"""
        raw_news = yf.Ticker(ticker).news or []
        normalized = []

        for news_item in raw_news[:MAX_NEWS_ITEMS]:
            if isinstance(news_item, dict):
                normalized.append(normalize_news_item(ticker, news_item))

        return normalized

    def save_news(self, ticker: str) -> tuple[bool, str]:
        """1銘柄分のニュースを取得し、JSONへ上書き保存します。"""
        output_path = self.output_dir / f"{ticker}.json"

        try:
            news = self.fetch_news(ticker)
            with output_path.open("w", encoding="utf-8") as file:
                json.dump(news, file, ensure_ascii=False, indent=2)

            return True, f"{ticker}: 保存完了 ({len(news)}件) -> {output_path}"
        except Exception as error:
            return False, f"{ticker}: エラー - {error}"

    def run(self) -> int:
        timezone_setting = get_timezone(self.settings)
        started_at = datetime.now(timezone_setting)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.logger.info("Compass v1.0-alpha - News fetch")
        self.logger.info("開始時刻: %s", started_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.logger.info("設定ファイル: %s", self.config_path)
        self.logger.info("保存先: %s", self.output_dir)
        self.logger.info("最大件数: %s", MAX_NEWS_ITEMS)

        try:
            tickers = load_tickers(self.config_path)
        except Exception as error:
            self.logger.exception("設定読み込みエラー: %s", error)
            return 1

        successful_tickers: list[str] = []
        failed_tickers: list[str] = []

        for ticker in tickers:
            ok, message = self.save_news(ticker)
            if ok:
                successful_tickers.append(ticker)
                self.logger.info("[OK] %s", message)
            else:
                failed_tickers.append(ticker)
                self.logger.error("[NG] %s", message)

        finished_at = datetime.now(timezone_setting)
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

    logger = setup_logger(PROJECT_ROOT, settings, "compass.news")
    collector = NewsCollector(PROJECT_ROOT, settings, logger)
    return collector.run()


if __name__ == "__main__":
    sys.exit(main())
