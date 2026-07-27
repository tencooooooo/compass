import json
import unittest
from pathlib import Path

from utils.news_sentiment import classify_text


FIXTURE_PATH = Path(__file__).parent / "fixtures" / "news_sentiment_labeled.json"


class NewsSentimentTest(unittest.TestCase):
    def test_labeled_fixture_accuracy_stays_above_threshold(self):
        rows = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        correct = sum(1 for row in rows if classify_text(row["text"]) == row["label"])
        accuracy = correct / len(rows)

        self.assertGreaterEqual(accuracy, 0.90)

    def test_word_boundaries_and_phrase_overrides(self):
        self.assertEqual(classify_text("Rainfall disrupts factory commute"), "neutral")
        self.assertEqual(classify_text("Company cuts costs after margin expansion plan"), "positive")
        self.assertEqual(classify_text("Company cuts guidance after weak demand"), "negative")
        self.assertEqual(classify_text("Analysts see no downgrade risk after results"), "positive")

    def test_mixed_signal_headlines_resolve_to_negative(self):
        """好材料語と悪材料語が同居する実際の見出しが、中立に薄まらないことを確認します。"""
        self.assertEqual(classify_text("Nvidia AI chip demand falls short as revenue misses estimates"), "negative")
        self.assertEqual(classify_text("Company posts record loss amid weak demand"), "negative")
        self.assertEqual(classify_text("Apple faces antitrust probe over AI partnership"), "negative")

    def test_ai_mention_alone_is_not_positive(self):
        """AI銘柄中心のユニバースで "AI" が無条件加点にならないことを確認します。"""
        self.assertEqual(classify_text("Company announces AI strategy update"), "neutral")
        self.assertEqual(classify_text("Regulator opens AI probe"), "negative")


if __name__ == "__main__":
    unittest.main()
