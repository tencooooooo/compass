import logging
import tempfile
import unittest
from pathlib import Path

from collectors.news.fetch_news import NewsCollector


class FakeNewsCollector(NewsCollector):
    """取得処理を差し替え、指定した銘柄だけ失敗させるテスト用collectorです。"""

    def __init__(self, project_root: Path, failing_tickers: set[str]):
        settings = {"timezone": "UTC", "output_directory": "storage"}
        logger = logging.getLogger("compass.test.news")
        logger.addHandler(logging.NullHandler())
        logger.propagate = False
        super().__init__(project_root, settings, logger)
        self.failing_tickers = failing_tickers

    def save_news(self, ticker: str) -> tuple[bool, str]:
        if ticker in self.failing_tickers:
            return False, f"{ticker}: エラー - テスト用の失敗"
        return True, f"{ticker}: 保存完了"


class FetchNewsExitCodeTest(unittest.TestCase):
    def setUp(self):
        self._tempdir = tempfile.TemporaryDirectory()
        self.project_root = Path(self._tempdir.name)
        config_dir = self.project_root / "config"
        config_dir.mkdir(parents=True)
        (config_dir / "tickers.yaml").write_text(
            "tickers:\n"
            "  - AAPL\n"
            "  - MSFT\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self._tempdir.cleanup()

    def run_collector(self, failing_tickers: set[str]) -> int:
        collector = FakeNewsCollector(self.project_root, failing_tickers)
        return collector.run()

    def test_all_success_returns_zero(self):
        self.assertEqual(self.run_collector(set()), 0)

    def test_partial_failure_returns_zero(self):
        # ニュースは補助データのため、一部失敗では後続処理を止めません。
        self.assertEqual(self.run_collector({"AAPL"}), 0)

    def test_all_failure_returns_one(self):
        self.assertEqual(self.run_collector({"AAPL", "MSFT"}), 1)


if __name__ == "__main__":
    unittest.main()
