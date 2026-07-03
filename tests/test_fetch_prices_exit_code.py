import logging
import tempfile
import unittest
from pathlib import Path

from collectors.prices.fetch_prices import PriceCollector


class FakePriceCollector(PriceCollector):
    """取得処理を差し替え、指定した銘柄だけ失敗させるテスト用collectorです。"""

    def __init__(self, project_root: Path, failing_tickers: set[str]):
        settings = {"timezone": "UTC", "output_directory": "storage"}
        logger = logging.getLogger("compass.test.prices")
        logger.addHandler(logging.NullHandler())
        logger.propagate = False
        super().__init__(project_root, settings, logger)
        self.failing_tickers = failing_tickers

    def save_ticker_prices(self, ticker: str) -> tuple[bool, str]:
        if ticker in self.failing_tickers:
            return False, f"{ticker}: エラー - テスト用の失敗"
        return True, f"{ticker}: 保存完了"


class FetchPricesExitCodeTest(unittest.TestCase):
    def setUp(self):
        self._tempdir = tempfile.TemporaryDirectory()
        self.project_root = Path(self._tempdir.name)
        config_dir = self.project_root / "config"
        config_dir.mkdir(parents=True)
        (config_dir / "tickers.yaml").write_text(
            "tickers:\n"
            "  - AAPL\n"
            "  - MSFT\n"
            "benchmarks:\n"
            "  - SPY\n"
            "  - XLK\n"
            "required_benchmarks:\n"
            "  - SPY\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self._tempdir.cleanup()

    def run_collector(self, failing_tickers: set[str]) -> int:
        collector = FakePriceCollector(self.project_root, failing_tickers)
        return collector.run()

    def test_all_success_returns_zero(self):
        self.assertEqual(self.run_collector(set()), 0)

    def test_watch_ticker_failure_returns_one(self):
        self.assertEqual(self.run_collector({"AAPL"}), 1)

    def test_required_benchmark_failure_returns_one(self):
        self.assertEqual(self.run_collector({"SPY"}), 1)

    def test_optional_benchmark_failure_returns_zero(self):
        self.assertEqual(self.run_collector({"XLK"}), 0)


if __name__ == "__main__":
    unittest.main()
