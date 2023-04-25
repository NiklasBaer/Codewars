import unittest

from ArrayPlusArray import array_plus_array

class TestArrayPlusArray(unittest.TestCase):
    
    def test_leere(self):
        self.assertEqual(array_plus_array([],[]),0)
        
    def test_even(self):
        self.assertEqual(array_plus_array([4,6,8,], [12,14,6]),50)
        
    def test_minusZahlen(self):
        self.assertEqual(array_plus_array([-3,-5,-8],[-123,-658]), -797)
    
        
        
        
if __name__ == "__main__" :
    unittest.main()