import unittest

import pandas as pd

from engines.discovery.candidate_selector import build_candidate


def price_frame(closes: list[float]) -> pd.DataFrame:
    dates = pd.bdate_range("2025-01-01", periods=len(closes))
    return pd.DataFrame(
        {
            "date": dates,
            "close": closes,
            "adj_close": closes,
            "volume": [1_000_000] * len(closes),
        }
    )


def rising_closes(rows: int = 300, daily_rate: float = 0.01) -> list[float]:
    return [100 * (1 + daily_rate) ** i for i in range(rows)]


def flat_closes(rows: int = 300) -> list[float]:
    return [100.0] * rows


def candidate_for(prices: pd.DataFrame, benchmark: pd.DataFrame | None, benchmark_name: str | None) -> dict:
    return build_candidate(
        ticker="TEST",
        company={},
        financials={},
        news_items=[],
        events=[],
        prices=prices,
        score_result={},
        company_report="",
        market_dashboard={},
        benchmark_prices=benchmark,
        benchmark_name=benchmark_name,
    )


class DiscoveryMomentumTest(unittest.TestCase):
    def test_relative_momentum_uses_benchmark(self):
        candidate = candidate_for(price_frame(rising_closes()), price_frame(flat_closes()), "SPY")

        self.assertEqual(candidate["metrics"]["benchmark"], "SPY")
        self.assertNotIn("benchmark_prices", candidate["missing_data"])
        for key in ("1m", "3m", "6m", "1y"):
            self.assertIsNotNone(candidate["metrics"]["excess_momentum"][key])
        self.assertTrue(any("市場を大きく上回っています" in reason for reason in candidate["discovery_reasons"]))

    def test_missing_benchmark_falls_back_to_absolute(self):
        candidate = candidate_for(price_frame(rising_closes()), None, None)

        self.assertIn("benchmark_prices", candidate["missing_data"])
        self.assertIsNone(candidate["metrics"]["benchmark"])
        self.assertTrue(any("絶対リターン" in point for point in candidate["watch_points"]))

    def test_laggard_in_rising_market_scores_lower_than_absolute(self):
        relative = candidate_for(price_frame(flat_closes()), price_frame(rising_closes()), "SPY")
        absolute = candidate_for(price_frame(flat_closes()), None, None)

        self.assertLess(relative["discovery_score"], absolute["discovery_score"])


if __name__ == "__main__":
    unittest.main()
