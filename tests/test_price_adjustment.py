from datetime import datetime, timezone
import unittest

import pandas as pd

from engines.validation.backtest_engine import calculate_return
from utils.price_data import trading_day_momentum


class PriceAdjustmentTest(unittest.TestCase):
    def test_calculate_return_uses_adjusted_close(self):
        prices = pd.DataFrame(
            [
                {"date": "2024-01-01", "close": 1000.0, "adj_close": 100.0, "volume": 1},
                {"date": "2024-01-31", "close": 100.0, "adj_close": 100.0, "volume": 1},
            ]
        )

        result = calculate_return(prices, datetime(2024, 1, 1, tzinfo=timezone.utc), 30)

        self.assertEqual(result["start_price"], 100.0)
        self.assertEqual(result["end_price"], 100.0)
        self.assertEqual(result["return_percent"], 0.0)

    def test_calculate_return_marks_missing_start_as_incomplete_when_gap_is_large(self):
        prices = pd.DataFrame([{"date": "2024-02-01", "close": 100.0, "adj_close": 100.0, "volume": 1}])

        result = calculate_return(prices, datetime(2024, 1, 1, tzinfo=timezone.utc), 30)

        self.assertFalse(result["period_complete"])
        self.assertIsNone(result["return_percent"])

    def test_trading_day_momentum_uses_21_rows_for_one_month(self):
        prices = pd.DataFrame(
            [{"date": f"2024-01-{day + 1:02d}", "close": 100.0 + day, "adj_close": 100.0 + day} for day in range(22)]
        )

        self.assertEqual(trading_day_momentum(prices, 30), 21.0)

    def test_trading_day_momentum_returns_none_when_data_is_short(self):
        prices = pd.DataFrame(
            [{"date": f"2024-01-{day + 1:02d}", "close": 100.0 + day, "adj_close": 100.0 + day} for day in range(21)]
        )

        self.assertIsNone(trading_day_momentum(prices, 30))


if __name__ == "__main__":
    unittest.main()
