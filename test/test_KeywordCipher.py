import unittest

from src.KeywordCipher import keyword_cipher

class TestKeywordCipher(unittest.TestCase):
    
    def test_langes_keyword(self):
        self.assertEqual(keyword_cipher("Hallo ich bins ", "HalloWarumtueichdashier"), "mHccs tlm atdj ")
        
        
        
    if __name__ == "__main__" :
        unittest.main()