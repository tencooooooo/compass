import unittest

from engines.validation.validation_report import render_validation_summary


def make_row(**overrides):
    row = {
        "ticker": "AAPL",
        "period": "1w",
        "discovery_score": 70,
        "return_percent": 10.0,
        "benchmark_diff_percent": 5.0,
        "sector_diff_percent": 5.0,
        "validation_result": "Excellent",
        "period_complete": True,
        "confidence": "High",
        "discovery_reasons": ["強い成長シグナル"],
        "watch_points": ["バリュエーションが高い"],
    }
    row.update(overrides)
    return row


class ValidationSummaryTest(unittest.TestCase):
    def test_result_counts_exclude_incomplete_rows(self):
        rows = [
            make_row(),
            make_row(validation_result="Poor", return_percent=-8.0),
            make_row(validation_result="Neutral", period_complete=False, return_percent=100.0),
        ]
        summary = render_validation_summary(rows, "2026-07-17", {"1w": 7}, "SPY")
        self.assertIn("- Excellent: 1", summary)
        self.assertIn("- Poor: 1", summary)
        self.assertIn("- Neutral: 0", summary)
        self.assertIn("- Pending(期間未完了): 1", summary)

    def test_average_return_uses_completed_rows_only(self):
        rows = [
            make_row(return_percent=10.0),
            make_row(validation_result="Neutral", period_complete=False, return_percent=100.0),
        ]
        summary = render_validation_summary(rows, "2026-07-17", {"1w": 7}, "SPY")
        self.assertIn("平均騰落率(期間完了分): 10.00%", summary)

    def test_features_come_from_completed_rows_only(self):
        rows = [
            make_row(validation_result="Neutral", period_complete=False, watch_points=["未完了のみの注意点"]),
            make_row(validation_result="Poor", watch_points=["完了済みの注意点"]),
        ]
        summary = render_validation_summary(rows, "2026-07-17", {"1w": 7}, "SPY")
        self.assertIn("完了済みの注意点", summary)
        self.assertNotIn("未完了のみの注意点", summary)

    def test_validation_rules_reflect_period_specific_thresholds(self):
        summary = render_validation_summary([make_row()], "2026-07-17", {"1w": 7, "1m": 30}, "SPY")
        self.assertIn("- 1w: Excellent 騰落率 3.0%以上 または ベンチマーク超過 2.0%以上", summary)
        self.assertIn("- 1m: Excellent 騰落率 6.0%以上", summary)
        self.assertNotIn("騰落率が15%以上", summary)


if __name__ == "__main__":
    unittest.main()
