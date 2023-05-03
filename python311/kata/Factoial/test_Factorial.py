import unittest

from python311.kata.Factoial.Factorial import factorial


class TestFactorial(unittest.TestCase):

    def test_wenn_null(self):
        self.assertEqual(factorial(0), 1)


if __name__ == "__main__":
    unittest.main()
