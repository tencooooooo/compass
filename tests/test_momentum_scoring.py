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
        # 全期間で市場を大きく上回る(各4点=16点)+通常水準の出来高(4点x0.75=3点)
        self.assertEqual(result["score"], 19)

    def test_max_score_is_actually_reachable(self):
        """max_score(20)が到達可能であることを保証します(以前は上限16点で構造的に到達不能でした)。"""
        closes = rising_closes()
        stock = price_frame(closes)
        # 直近1日だけ出来高を増やし、30日平均比1.2倍以上の満点条件を作ります。
        stock.loc[stock.index[-1], "volume"] = 100_000_000
        benchmark = price_frame(flat_closes())

        result = calculate_momentum(stock, benchmark, "SPY")

        self.assertEqual(result["score"], result["max_score"])

    def test_missing_volume_column_does_not_raise(self):
        """volume列を持たない価格CSVでも、銘柄ごと例外で落とさないことを確認します。"""
        stock = price_frame(rising_closes()).drop(columns=["volume"])

        result = calculate_momentum(stock, price_frame(flat_closes()), "SPY")

        self.assertIn("volume", result["missing_data"])
        self.assertGreater(result["score"], 0)

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
