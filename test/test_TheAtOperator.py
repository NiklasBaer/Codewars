import unittest

from src.TheAtOperator import evaluate
@unittest.skip("Kommt später wieder")
class TestTheAtOperator(unittest.TestCase):
    
    def test_wenn_null(self):
        self.assertEqual(evaluate("0 @ 0"), None)
        
    def test_wenn_erste_null(self):
        self.assertEqual(evaluate("0@4"), 0)
        
    def test_wenn_zweite_null(self):
        self.assertEqual(evaluate("12@0"), None)
        
    def test_wenn_mehr_als_eins(self):
        self.assertEqual(evaluate("3@3@3"), 16)
        
    def test_wenn_minus_Zahlen(self):
        self.assertEqual(evaluate("1@1@-4"), -9)
        
        
        
if __name__ == "__main__":
    unittest.main()