import unittest

from engines.scoring_engine.score_calculator import calculate_valuation, percentile_rank_lower_is_better


class ValuationScoringTest(unittest.TestCase):
    def test_percentile_rank_lower_is_better(self):
        self.assertEqual(percentile_rank_lower_is_better(10, [10, 20, 30, 40, 50]), 0.0)
        self.assertEqual(percentile_rank_lower_is_better(50, [10, 20, 30, 40, 50]), 100.0)

    def test_sector_relative_valuation_scores_low_percentile(self):
        peers = [
            {"sector": "Technology", "trailing_pe": 10, "forward_pe": 10, "peg_ratio": 0.8, "price_to_book": 4},
            {"sector": "Technology", "trailing_pe": 20, "forward_pe": 20, "peg_ratio": 1.2, "price_to_book": 8},
            {"sector": "Technology", "trailing_pe": 30, "forward_pe": 30, "peg_ratio": 1.8, "price_to_book": 12},
            {"sector": "Technology", "trailing_pe": 40, "forward_pe": 40, "peg_ratio": 2.5, "price_to_book": 16},
            {"sector": "Technology", "trailing_pe": 50, "forward_pe": 50, "peg_ratio": 3.0, "price_to_book": 20},
        ]

        result = calculate_valuation(peers[0], peers)

        self.assertEqual(result["metrics"]["sector_peer_count"], 5)
        self.assertEqual(result["metrics"]["trailing_pe_percentile"], 0.0)
        self.assertGreaterEqual(result["score"], 15)
        self.assertTrue(any("母数 5" in reason for reason in result["reasons"]))

    def test_small_sector_falls_back_to_fixed_thresholds(self):
        company = {"trailing_pe": 20, "forward_pe": 20, "peg_ratio": 1.5, "price_to_book": 10}

        result = calculate_valuation(company, [company, company])

        self.assertEqual(result["metrics"]["sector_peer_count"], 2)
        self.assertTrue(any("固定閾値" in reason for reason in result["reasons"]))


if __name__ == "__main__":
    unittest.main()
