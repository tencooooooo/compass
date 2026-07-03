from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from collectors.financials.cross_check import revenue_cross_check
from collectors.news.build_event_database import parse_news_date
from utils.news_dedup import dedupe_news_items
from utils.tickers import load_benchmarks, load_tickers


class LoadBenchmarksTest(unittest.TestCase):
    def _write_config(self, tmp_dir: str, content: str) -> Path:
        path = Path(tmp_dir) / "tickers.yaml"
        path.write_text(content, encoding="utf-8")
        return path

    def test_loads_benchmarks_separately_from_tickers(self):
        with TemporaryDirectory() as tmp_dir:
            path = self._write_config(tmp_dir, "tickers:\n  - AAPL\nbenchmarks:\n  - spy\n  - XLK\n")

            self.assertEqual(load_tickers(path), ["AAPL"])
            self.assertEqual(load_benchmarks(path), ["SPY", "XLK"])

    def test_missing_benchmarks_returns_empty_list(self):
        with TemporaryDirectory() as tmp_dir:
            path = self._write_config(tmp_dir, "tickers:\n  - AAPL\n")

            self.assertEqual(load_benchmarks(path), [])

    def test_repo_config_includes_spy(self):
        config_path = Path(__file__).resolve().parents[1] / "config" / "tickers.yaml"

        benchmarks = load_benchmarks(config_path)

        self.assertIn("SPY", benchmarks)
        self.assertNotIn("SPY", load_tickers(config_path))


class NewsMarketHoursAttributionTest(unittest.TestCase):
    def test_news_during_market_hours_stays_on_same_day(self):
        # 10:00 ET = 14:00 UTC(夏時間)
        attributed = parse_news_date("2026-06-15T14:00:00Z")
        self.assertEqual(attributed.strftime("%Y-%m-%d"), "2026-06-15")

    def test_news_after_market_close_moves_to_next_day(self):
        # 18:00 ET = 22:00 UTC(夏時間)は引け後なので翌日に帰属
        attributed = parse_news_date("2026-06-15T22:00:00Z")
        self.assertEqual(attributed.strftime("%Y-%m-%d"), "2026-06-16")

    def test_late_utc_news_is_not_double_shifted(self):
        # 23:30 UTC = 19:30 ET(同日)→ 引け後なので翌日
        attributed = parse_news_date("2026-06-15T23:30:00Z")
        self.assertEqual(attributed.strftime("%Y-%m-%d"), "2026-06-16")

    def test_invalid_dates_return_none(self):
        self.assertIsNone(parse_news_date(None))
        self.assertIsNone(parse_news_date("not a date"))


class NewsDedupTest(unittest.TestCase):
    def test_removes_syndicated_duplicates(self):
        items = [
            {"title": "Apple Beats Q2 Estimates", "publisher": "Reuters"},
            {"title": "Apple beats Q2 estimates!", "publisher": "Yahoo"},
            {"title": "Different story", "publisher": "Reuters"},
        ]

        unique_items = dedupe_news_items(items)

        self.assertEqual(len(unique_items), 2)
        self.assertEqual(unique_items[0]["publisher"], "Reuters")

    def test_keeps_items_without_titles(self):
        items = [{"title": None}, {"title": ""}, {"title": "Real"}]

        self.assertEqual(len(dedupe_news_items(items)), 3)


class RevenueCrossCheckTest(unittest.TestCase):
    def test_flags_quarters_with_large_revenue_gap(self):
        sec_rows = [
            {"fiscal_quarter": "2026-Q1", "total_revenue": 100.0},
            {"fiscal_quarter": "2025-Q4", "total_revenue": 90.0},
        ]
        yfinance_rows = [
            {"fiscal_quarter": "2026-Q1", "total_revenue": 130.0},
            {"fiscal_quarter": "2025-Q4", "total_revenue": 91.0},
        ]

        result = revenue_cross_check(sec_rows, yfinance_rows)

        self.assertEqual(result["checked_quarters"], 2)
        self.assertEqual(len(result["mismatches"]), 1)
        self.assertEqual(result["mismatches"][0]["fiscal_quarter"], "2026-Q1")
        self.assertEqual(result["mismatches"][0]["diff_percent"], 30.0)

    def test_skips_quarters_missing_on_either_side(self):
        sec_rows = [{"fiscal_quarter": "2026-Q1", "total_revenue": 100.0}]

        result = revenue_cross_check(sec_rows, [])

        self.assertEqual(result["checked_quarters"], 0)
        self.assertEqual(result["mismatches"], [])

    def test_handles_non_list_inputs(self):
        result = revenue_cross_check(None, None)

        self.assertEqual(result["checked_quarters"], 0)
        self.assertEqual(result["mismatches"], [])


if __name__ == "__main__":
    unittest.main()
