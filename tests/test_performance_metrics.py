import unittest

from lab.performance.metrics import PerformanceMetrics


class PerformanceMetricsTest(unittest.TestCase):
    def test_validation_distribution_prefers_existing_validation_result(self):
        rows = [
            {
                "status": "completed",
                "confidence": "High",
                "return_percent": 20.0,
                "validation_result": "Neutral",
            }
        ]

        distribution = PerformanceMetrics().validation_distribution_by(rows, "confidence")

        self.assertEqual(distribution["High"]["validation_results"]["Neutral"], 1)
        self.assertEqual(distribution["High"]["validation_results"]["Excellent"], 0)

    def test_fallback_classification_uses_period_specific_thresholds(self):
        # 7日行はValidation Engineの1w閾値(Excellent 3.0%)で分類される。旧来の一律15%ではNeutralになっていた。
        rows = [
            {"status": "completed", "confidence": "High", "period": 7, "return_percent": 3.5},
            {"status": "completed", "confidence": "High", "period": 365, "return_percent": 3.5},
        ]

        distribution = PerformanceMetrics().validation_distribution_by(rows, "confidence")

        self.assertEqual(distribution["High"]["validation_results"]["Excellent"], 1)
        self.assertEqual(distribution["High"]["validation_results"]["Neutral"], 1)

    def test_summarize_reports_ticker_equal_weight_metrics(self):
        # NVDAの完了3行が平均を支配しないよう、銘柄内平均→銘柄間等重み平均の順で計算される。
        rows = [
            {"status": "completed", "ticker": "NVDA", "return_percent": 10.0, "alpha_percent": 9.0},
            {"status": "completed", "ticker": "NVDA", "return_percent": 8.0, "alpha_percent": 7.0},
            {"status": "completed", "ticker": "NVDA", "return_percent": 12.0, "alpha_percent": 11.0},
            {"status": "completed", "ticker": "INTC", "return_percent": -4.0, "alpha_percent": -5.0},
            {"status": "pending", "ticker": "AMZN", "return_percent": None, "alpha_percent": None},
        ]

        summary = PerformanceMetrics().summarize(rows)

        self.assertEqual(summary["unique_ticker_count"], 3)
        self.assertEqual(summary["completed_ticker_count"], 2)
        self.assertEqual(summary["ticker_equal_weight_average_return"], 3.0)
        self.assertEqual(summary["ticker_equal_weight_alpha"], 2.0)
        self.assertEqual(summary["ticker_equal_weight_win_rate"], 50.0)

    def test_summarize_without_ticker_fields_returns_none_equal_weight(self):
        rows = [{"status": "completed", "return_percent": 4.0}]

        summary = PerformanceMetrics().summarize(rows)

        self.assertEqual(summary["unique_ticker_count"], 0)
        self.assertIsNone(summary["ticker_equal_weight_alpha"])

    def test_summarize_reports_worst_return_of_completed_rows(self):
        rows = [
            {"status": "completed", "return_percent": 4.0},
            {"status": "completed", "return_percent": -6.5},
            {"status": "pending", "return_percent": None},
        ]

        summary = PerformanceMetrics().summarize(rows)

        self.assertEqual(summary["worst_return"], -6.5)
        self.assertNotIn("max_drawdown", summary)


if __name__ == "__main__":
    unittest.main()
