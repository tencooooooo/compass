import unittest

from engines.scoring_engine.score_calculator import calculate_news


def positive_items(count: int) -> list[dict[str, str]]:
    return [{"title": f"Company beats expectations in segment {index}"} for index in range(count)]


def negative_items(count: int) -> list[dict[str, str]]:
    return [{"title": f"Company faces lawsuit over product {index}"} for index in range(count)]


def neutral_items(count: int) -> list[dict[str, str]]:
    return [{"title": f"Company schedules quarterly report session {index}"} for index in range(count)]


class NewsScoringTest(unittest.TestCase):
    def test_sentiment_is_normalized_by_classified_count(self):
        small_coverage = calculate_news(positive_items(2) + negative_items(1), [])
        large_coverage = calculate_news(positive_items(8) + negative_items(4), [])

        # 同じ純比率なら、報道量が違ってもセンチメント評価は同じになる
        self.assertEqual(small_coverage["metrics"]["sentiment_net_ratio"], 0.33)
        self.assertEqual(large_coverage["metrics"]["sentiment_net_ratio"], 0.33)
        self.assertTrue(any("純比率" in reason for reason in small_coverage["reasons"]))

    def test_mixed_high_volume_news_does_not_inflate_sentiment(self):
        # 旧ロジック(4 + 好材料 - 悪材料)では 10-8=+2 で 6/8 点に膨らんでいたケース
        result = calculate_news(positive_items(10) + negative_items(8), [])

        self.assertEqual(result["metrics"]["sentiment_net_ratio"], 0.11)
        # coverage 上限 6 点 + 中立寄りセンチメント(約4.4点)で、10点前後にとどまる
        self.assertLessEqual(result["score"], 11)

    def test_negative_dominant_news_scores_low(self):
        result = calculate_news(negative_items(5), [])

        self.assertEqual(result["metrics"]["sentiment_net_ratio"], -1.0)
        self.assertLessEqual(result["score"], 2)

    def test_unclassifiable_news_is_neutral(self):
        result = calculate_news(neutral_items(4), [])

        self.assertIsNone(result["metrics"]["sentiment_net_ratio"])
        self.assertTrue(any("中立の4.0点" in reason for reason in result["reasons"]))


if __name__ == "__main__":
    unittest.main()
