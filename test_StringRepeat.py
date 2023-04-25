import unittest

from StringRepeat import repeat_str

class TestStringRepeat(unittest.TestCase):
    
    def test_null(self):
        self.assertEqual(repeat_str(0, "a"), "")
        
    def test_even_Zahl(self):
        self.assertEqual(repeat_str(12, "b"), "bbbbbbbbbbbb")
        
    def test_odd_Zahl(self):
        self.assertEqual(repeat_str(7, "z"), "zzzzzzz")
        
    def test_mehrAlsEinBuchstabe(self):
        self.assertEqual(repeat_str(3, "ert"), "ertertert")
        
        
if __name__ == "__main__" :
    unittest.main()