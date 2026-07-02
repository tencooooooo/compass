import unittest

from engines.scoring_engine.score_calculator import calculate_growth, yoy_growth


class GrowthScoringTest(unittest.TestCase):
    def test_yoy_growth_calculates_normal_case(self):
        self.assertEqual(yoy_growth(130, 100), 30.0)
        self.assertEqual(yoy_growth(80, 100), -20.0)

    def test_yoy_growth_handles_zero_or_missing_prior(self):
        self.assertIsNone(yoy_growth(100, 0))
        self.assertIsNone(yoy_growth(None, 100))

    def test_calculate_growth_uses_quarterly_yoy_metrics(self):
        result = calculate_growth(
            {
                "total_revenue": 130,
                "eps": 2.0,
                "net_income": 20,
                "operating_income": 25,
                "research_and_development": 5,
                "quarterly_financials": [
                    {"fiscal_quarter": "2026-Q2", "total_revenue": 130, "eps": 2.0},
                    {"fiscal_quarter": "2026-Q1", "total_revenue": 125, "eps": 1.8},
                    {"fiscal_quarter": "2025-Q4", "total_revenue": 115, "eps": 1.4},
                    {"fiscal_quarter": "2025-Q3", "total_revenue": 120, "eps": 1.6},
                    {"fiscal_quarter": "2025-Q2", "total_revenue": 100, "eps": 1.0},
                ],
            }
        )

        self.assertEqual(result["metrics"]["revenue_yoy_growth"], 30.0)
        self.assertEqual(result["metrics"]["eps_yoy_growth"], 100.0)
        self.assertNotIn("revenue_growth", result["missing_data"])

    def test_calculate_growth_falls_back_when_quarterly_series_missing(self):
        result = calculate_growth(
            {
                "total_revenue": 100,
                "eps": 1,
                "net_income": 10,
                "operating_income": 12,
                "research_and_development": 3,
            }
        )

        self.assertIn("revenue_growth", result["missing_data"])
        self.assertIsNone(result["metrics"]["revenue_yoy_growth"])
        self.assertTrue(any("フォールバック" in reason for reason in result["reasons"]))


if __name__ == "__main__":
    unittest.main()
