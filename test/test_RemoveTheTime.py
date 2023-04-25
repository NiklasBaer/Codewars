import unittest

from src.RemoveTheTime import shorten_to_date

class TestRemoveTheTime(unittest.TestCase):
    
    def test_Zeit(self):
        self.assertEqual(shorten_to_date("Montag Oktober 2,9pm"), "Montag Oktober 2")
        
    def test_Zeit2(self):
        self.assertEqual(shorten_to_date("Donnerstag Janur 4, 12am"), "Donnerstag Janur 4")
        
    def test_Zeit3(self):
        self.assertEqual(shorten_to_date("Freitag Dezember 4, 9am"), "Freitag Dezember 4")
    
        
        
if __name__ == "__main__" :
    unittest.main()