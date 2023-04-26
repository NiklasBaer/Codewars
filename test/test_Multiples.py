import unittest

from src.Multiples import multiple

class TestMultiples(unittest.TestCase):
    
    def test_wenn_string(self):
        self.assertEqual(multiple("2"), "Miss")
        
    def test_wenn_null(self):
        self.assertEqual(multiple(0), "Miss")
        
    def test_wenn_liste(self):
        self.assertEqual(multiple([]), [])
        
        
if __name__ == "__main__" : 
    unittest.main()