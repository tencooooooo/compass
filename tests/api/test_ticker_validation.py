import unittest

from api.services.compass_data import _ticker


class TickerValidationTest(unittest.TestCase):
    def test_valid_ticker_is_normalized(self):
        self.assertEqual(_ticker(" nvda "), "NVDA")
        self.assertEqual(_ticker("BRK-B"), "BRK-B")

    def test_windows_path_separator_is_rejected(self):
        with self.assertRaises(ValueError):
            _ticker("..\\..\\knowledge\\api")

    def test_forward_path_separator_is_rejected(self):
        with self.assertRaises(ValueError):
            _ticker("../../knowledge/api")


if __name__ == "__main__":
    unittest.main()

