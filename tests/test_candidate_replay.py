import unittest

from lab.experiments.candidate_replay import (
    baseline_momentum_award,
    momentum_taper_delta,
    news_cap_delta,
    tapered_momentum_award,
)


class MomentumTaperTest(unittest.TestCase):
    def test_baseline_award_matches_candidate_selector_tiers(self):
        self.assertEqual(baseline_momentum_award(12.0, 8, relative=True), 8)
        self.assertEqual(baseline_momentum_award(5.0, 8, relative=True), 8 * 0.65)
        self.assertEqual(baseline_momentum_award(-5.0, 8, relative=True), 8 * 0.25)
        self.assertEqual(baseline_momentum_award(-15.0, 8, relative=True), 0)
        self.assertEqual(baseline_momentum_award(16.0, 8, relative=False), 8)

    def test_taper_reduces_only_overextended_awards(self):
        # +35ptの超過は満点ではなく0.25×ティアに落ちる。+12ptは従来どおり満点。
        self.assertEqual(tapered_momentum_award(35.0, 8, relative=True), 8 * 0.25)
        self.assertEqual(tapered_momentum_award(12.0, 8, relative=True), 8)
        self.assertEqual(tapered_momentum_award(-5.0, 8, relative=True), 8 * 0.25)

    def test_momentum_taper_delta_uses_excess_momentum_when_benchmark_present(self):
        metrics = {
            "benchmark": "SPY",
            "momentum": {"1m": 2.7, "3m": 14.4, "6m": 149.8, "1y": 178.9},
            "excess_momentum": {"1m": -0.7, "3m": 10.4, "6m": 135.2, "1y": 157.2},
        }
        # 6m(5点)と1y(8点)だけが満点→0.25×に落ちる: (1.25-5) + (2-8) = -9.75
        self.assertAlmostEqual(momentum_taper_delta(metrics), -9.75)

    def test_momentum_taper_delta_falls_back_to_absolute_momentum(self):
        metrics = {
            "benchmark": None,
            "momentum": {"1m": 40.0, "3m": None, "6m": 10.0, "1y": None},
            "excess_momentum": {"1m": None, "3m": None, "6m": None, "1y": None},
        }
        # 1m(4点)は40%で満点→0.25×(-3.0)。6mは10%でどちらも0.65×なので差分なし。
        self.assertAlmostEqual(momentum_taper_delta(metrics), -3.0)

    def test_momentum_taper_delta_is_zero_for_calm_momentum(self):
        metrics = {
            "benchmark": "SPY",
            "momentum": {"1m": 3.0, "3m": 15.0, "6m": 8.6, "1y": 12.0},
            "excess_momentum": {"1m": 1.0, "3m": 12.0, "6m": 5.0, "1y": 8.0},
        }
        self.assertEqual(momentum_taper_delta(metrics), 0.0)


class NewsCapTest(unittest.TestCase):
    def test_news_above_cap_is_reduced_proportionally(self):
        # 18/20 -> 16/20: (16-18)/20 * 8点 = -0.8
        self.assertAlmostEqual(news_cap_delta({"news_score": 18.0}), -0.8)

    def test_news_at_or_below_cap_is_unchanged(self):
        self.assertEqual(news_cap_delta({"news_score": 16.0}), 0.0)
        self.assertEqual(news_cap_delta({"news_score": 14.0}), 0.0)
        self.assertEqual(news_cap_delta({"news_score": None}), 0.0)
        self.assertEqual(news_cap_delta({}), 0.0)


if __name__ == "__main__":
    unittest.main()
