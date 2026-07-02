import unittest

from utils.values import safe_float


class SafeFloatTest(unittest.TestCase):
    def test_converts_numeric_strings(self):
        self.assertEqual(safe_float("1.5"), 1.5)
        self.assertEqual(safe_float(3), 3.0)

    def test_returns_none_for_invalid_values(self):
        self.assertIsNone(safe_float(None))
        self.assertIsNone(safe_float("abc"))
        self.assertIsNone(safe_float([]))

    def test_returns_none_for_nan(self):
        self.assertIsNone(safe_float(float("nan")))


if __name__ == "__main__":
    unittest.main()
