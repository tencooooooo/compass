import unittest

import pandas as pd

from utils.price_data import validate_price_frame


def frame(rows: list[dict]) -> pd.DataFrame:
    return pd.DataFrame(rows)


class PriceValidationTest(unittest.TestCase):
    def test_clean_frame_passes_without_issues(self):
        prices = frame(
            [
                {"date": "2026-01-02", "open": 10, "high": 11, "low": 9, "close": 10.5, "adj_close": 10.5, "volume": 100},
                {"date": "2026-01-03", "open": 10.5, "high": 12, "low": 10, "close": 11.0, "adj_close": 11.0, "volume": 120},
            ]
        )

        validated, issues = validate_price_frame(prices)

        self.assertEqual(len(validated), 2)
        self.assertEqual(issues, [])

    def test_drops_contradictory_rows(self):
        prices = frame(
            [
                {"date": "2026-01-02", "open": 10, "high": 11, "low": 9, "close": 10.5, "adj_close": 10.5, "volume": 100},
                {"date": "2026-01-03", "open": 10, "high": 9, "low": 11, "close": 10.0, "adj_close": 10.0, "volume": 100},
                {"date": "2026-01-04", "open": 10, "high": 11, "low": 9, "close": -5.0, "adj_close": -5.0, "volume": 100},
                {"date": "2026-01-05", "open": 10, "high": 11, "low": 9, "close": 10.0, "adj_close": 10.0, "volume": -10},
            ]
        )

        validated, issues = validate_price_frame(prices)

        self.assertEqual(len(validated), 1)
        self.assertEqual(validated.iloc[0]["date"].strftime("%Y-%m-%d"), "2026-01-02")
        self.assertTrue(any("除外" in issue for issue in issues))

    def test_flags_extreme_moves_without_dropping(self):
        prices = frame(
            [
                {"date": "2026-01-02", "open": 100, "high": 101, "low": 99, "close": 100, "adj_close": 100, "volume": 100},
                {"date": "2026-01-03", "open": 100, "high": 200, "low": 99, "close": 200, "adj_close": 200, "volume": 100},
            ]
        )

        validated, issues = validate_price_frame(prices)

        self.assertEqual(len(validated), 2)
        self.assertTrue(any("要確認" in issue for issue in issues))

    def test_empty_frame_returns_empty(self):
        validated, issues = validate_price_frame(pd.DataFrame())

        self.assertTrue(validated.empty)
        self.assertEqual(issues, [])


if __name__ == "__main__":
    unittest.main()
