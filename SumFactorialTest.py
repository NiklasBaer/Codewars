
import unittest

from SumFactorial import sum_factorial

class TestSumFactorial(unittest.TestCase):
    
    def test_null(self):
        self.assertEqual(sum_factorial([0, 0]) , 2)
    
    def test_even(self):
        self.assertEqual(sum_factorial([4, 8]), 40344)
        
    def test_odd(self):
        self.assertEqual(sum_factorial([3,5]), 126)
        
        
        
if __name__ == "__main__" :
    unittest.main()