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

        self.assertGreaterEqual(accuracy, 0.70)

    def test_word_boundaries_and_phrase_overrides(self):
        self.assertEqual(classify_text("Rainfall disrupts factory commute"), "neutral")
        self.assertEqual(classify_text("Company cuts costs after margin expansion plan"), "positive")
        self.assertEqual(classify_text("Company cuts guidance after weak demand"), "negative")
        self.assertEqual(classify_text("Analysts see no downgrade risk after results"), "positive")


if __name__ == "__main__":
    unittest.main()
