import unittest

import pandas as pd

from engines.scoring_engine.score_calculator import calculate_momentum


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


class MomentumScoringTest(unittest.TestCase):
    def test_relative_scoring_rewards_outperformance(self):
        stock = price_frame(rising_closes())
        benchmark = price_frame(flat_closes())

        result = calculate_momentum(stock, benchmark, "SPY")

        self.assertEqual(result["metrics"]["benchmark"], "SPY")
        self.assertNotIn("benchmark_prices", result["missing_data"])
        for label in ("1M", "3M", "6M", "1Y"):
            self.assertIsNotNone(result["metrics"]["excess_returns"][label])
        self.assertTrue(any("超過リターン" in reason for reason in result["reasons"]))
        # 全期間で市場を大きく上回る(各3点)+通常水準の出来高(3点)
        self.assertEqual(result["score"], 15)

    def test_missing_benchmark_falls_back_to_absolute_returns(self):
        stock = price_frame(rising_closes())

        result = calculate_momentum(stock)

        self.assertIn("benchmark_prices", result["missing_data"])
        self.assertIsNone(result["metrics"]["benchmark"])
        self.assertTrue(any("絶対リターン" in reason for reason in result["reasons"]))

    def test_laggard_in_rising_market_scores_lower_than_absolute(self):
        stock = price_frame(flat_closes())
        benchmark = price_frame(rising_closes())

        relative = calculate_momentum(stock, benchmark, "SPY")
        absolute = calculate_momentum(stock)

        # 市場が大きく上昇する局面では、横ばい銘柄は絶対評価より低いスコアになる
        self.assertLess(relative["score"], absolute["score"])
        for label in ("1M", "3M", "6M", "1Y"):
            self.assertLess(relative["metrics"]["excess_returns"][label], -10)


if __name__ == "__main__":
    unittest.main()
