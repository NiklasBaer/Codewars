import unittest

from python311.kata.SimpleMultiplication.SimpleMultiplication import simple_multiplication


class TestSimpleMultiplication(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(
            simple_multiplication(0), 0,
            "Multiplikation mit 0 muss immer 0 ergeben.")

    def test_even_number(self):
        self.assertEqual(
            simple_multiplication(14), 112,
            "Eine gerade Zahl sollte mit 8 multipliziert werden.")

    def test_odd_number(self):
        self.assertEqual(
            simple_multiplication(3), 27,
            "Eine ungerade Zahl sollte mit 9 multipliziert werden.")


if __name__ == '__main__':
    unittest.main()
