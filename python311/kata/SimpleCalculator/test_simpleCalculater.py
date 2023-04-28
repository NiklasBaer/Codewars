import unittest

from python311.kata.SimpleCalculator.simpleCalculater import calculator

class TestSimpleCalculator(unittest.TestCase):
    
    def test_wenn_null(self):
        self.assertEqual(calculator(0,0, "+"),0)
    
        
if __name__ == "__main__":
    unittest.main()