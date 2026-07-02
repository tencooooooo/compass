import unittest
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from api.services import compass_data


class CompassDataCacheTest(unittest.TestCase):
    def setUp(self):
        compass_data._read_json_by_mtime.cache_clear()

    def test_score_results_reload_when_mtime_changes(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "company_scores.json"
            path.write_text('{"results": [{"ticker": "AAPL", "total_score": 10}]}', encoding="utf-8")
            os.utime(path, (1000, 1000))
            with patch.object(compass_data, "resolve_path", lambda relative_path: path):
                self.assertEqual(compass_data._score_results()[0]["total_score"], 10)
                path.write_text('{"results": [{"ticker": "AAPL", "total_score": 20}]}', encoding="utf-8")
                os.utime(path, (1000, 1000))
                self.assertEqual(compass_data._score_results()[0]["total_score"], 10)
                os.utime(path, (2000, 2000))
                self.assertEqual(compass_data._score_results()[0]["total_score"], 20)

    def test_invalid_generated_ticker_rows_do_not_break_lookup(self):
        with patch.object(
            compass_data,
            "_score_results",
            lambda: [{"ticker": "", "total_score": 1}, {"ticker": "..\\bad", "total_score": 2}, {"ticker": "AAPL", "total_score": 99}],
        ):
            with patch.object(compass_data, "_discovery_candidates", lambda: []):
                with patch.object(compass_data, "_validation_rows", lambda: []):
                    self.assertEqual(compass_data.get_score("AAPL")["total_score"], 99)
                    self.assertIsInstance(compass_data.get_companies(), list)


if __name__ == "__main__":
    unittest.main()
