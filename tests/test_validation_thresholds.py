import unittest

from engines.validation.backtest_engine import VALIDATION_THRESHOLDS, classify_result, threshold_note


class ValidationThresholdTest(unittest.TestCase):
    def test_period_specific_return_boundaries(self):
        for period, threshold in VALIDATION_THRESHOLDS.items():
            with self.subTest(period=period):
                self.assertEqual(classify_result(threshold["excellent"], None, True, period), "Excellent")
                self.assertEqual(classify_result(threshold["good"], None, True, period), "Good")
                self.assertEqual(classify_result(threshold["poor"], None, True, period), "Poor")

    def test_period_specific_benchmark_boundaries(self):
        for period, threshold in VALIDATION_THRESHOLDS.items():
            with self.subTest(period=period):
                self.assertEqual(classify_result(0.0, threshold["benchmark_excellent"], True, period), "Excellent")
                self.assertEqual(classify_result(0.0, threshold["benchmark_good"], True, period), "Good")
                self.assertEqual(classify_result(0.0, threshold["benchmark_poor"], True, period), "Poor")

    def test_incomplete_period_is_neutral(self):
        self.assertEqual(classify_result(100.0, 100.0, False, "1y"), "Neutral")

    def test_threshold_note_includes_period_and_values(self):
        note = threshold_note("1m")
        self.assertIn("1m", note)
        self.assertIn("Excellent", note)
        self.assertIn("benchmark diff", note)


if __name__ == "__main__":
    unittest.main()
