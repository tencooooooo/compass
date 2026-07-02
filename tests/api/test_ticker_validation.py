import unittest

from api.services.compass_data import normalize_ticker, validate_ticker


class TickerValidationTest(unittest.TestCase):
    def test_valid_ticker_is_normalized(self):
        self.assertEqual(validate_ticker(" nvda "), "NVDA")
        self.assertEqual(validate_ticker("BRK-B"), "BRK-B")

    def test_windows_path_separator_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_ticker("..\\..\\knowledge\\api")

    def test_forward_path_separator_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_ticker("../../knowledge/api")

    def test_generated_data_ticker_normalization_is_non_throwing(self):
        self.assertIsNone(normalize_ticker("..\\bad"))
        self.assertIsNone(normalize_ticker(""))
        self.assertEqual(normalize_ticker(" aapl "), "AAPL")


if __name__ == "__main__":
    unittest.main()
