import unittest

from RemoveFirstAndLastCharacter import remove_char

class TestRemoveFirstAndLastCharacter(unittest.TestCase):
    
    def test_String(self):
        self.assertEqual(remove_char("Hallo ich bins"), "allo ich bin")
        
    def test_Zahl(self):
        self.assertEqual(remove_char("12324"), "232")
        
        
        
if __name__ == "__main__": 
    unittest.main()