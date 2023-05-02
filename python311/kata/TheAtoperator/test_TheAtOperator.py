import unittest

from python311.kata.TheAtoperator.TheAtOperator import evaluate


class TestTheAtOperator(unittest.TestCase):

    def test_wenn_leer(self):
        self.assertEqual(evaluate(""), None)

    def test_wenn_null(self):
        self.assertEqual(evaluate("0"), 0)

    def test_wenn_zweite(self):
        self.assertEqual(evaluate("1 @ 0"), None)

    def test_wenn_beides_leer(self):
        self.assertEqual(evaluate("0 @ 0"), None)

    def test_wenn_erstes_null(self):
        self.assertEqual(evaluate("0 @ 5"), 0)

    def test_even_zahlen(self):
        self.assertEqual(evaluate("4 @ 6"), 32)

    def test_odd_zahlen(self):
        self.assertEqual(evaluate("3 @ 5"), 21)

    def test_wenn_mehr_als_zwei_zahlen(self):
        self.assertEqual(evaluate("8 @ 4 @ 4"), 312)

    def test_wenn_eine_von_vielen_null(self):
        self.assertEqual(evaluate("8 @ 5 @ 4 @ 3 @ 0 @ 5"), None)

    def test_wenn_zwei_null_sind(self):
        self.assertEqual(evaluate("8 @ 5 @ 4 @ 3 @ 0 @ 5 @ 9 @ 3 @ 0"), None)

    def test_wenn_erste_null(self):
        self.assertEqual(evaluate("0 @ 18"), 0)

    def test_wenn_nur_eine_zahl(self):
        self.assertEqual(evaluate("31"), 31)


if __name__ == "__main__":
    unittest.main()
