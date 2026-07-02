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


if __name__ == "__main__":
    unittest.main()
