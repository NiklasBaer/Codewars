import unittest

from SimpleMultiplication import simple_multiplication

class TestSimpleMultiplication(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(simple_multiplication(0), 0)

    def test_even_number(self):
        self.assertEqual(simple_multiplication(14), 112)
    
    def test_even_number(self):
        self.assertEqual(simple_multiplication(3), 27)

if __name__ == '__main__':
    unittest.main()