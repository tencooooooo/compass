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
