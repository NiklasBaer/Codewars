import unittest

from src.ZeichenRotiere import ZeichenRotierer

class TestStringUmdreher(unittest.TestCase):
    
    def test_leeren_string(self):
        x = ZeichenRotierer("")
        y = x.Rotiere()
        self.assertEqual(y, "")
        
    def test_einzelnen_Zeichen(self):
        x = ZeichenRotierer("1")
        y = x.Rotiere()
        self.assertEqual(y, [None])
        x =ZeichenRotierer("7")
        y = x.Rotiere()
        self.assertEqual(y, [None])
        
    def test_mehrere_Zeichen(self):
        x = ZeichenRotierer("22")
        y = x.Rotiere()
        self.assertEqual(y, ["2", "2"])
        x = ZeichenRotierer("227")
        y = x.Rotiere()
        self.assertEqual(y, ["2", "2", None])
    
        
if __name__ == "__main__":
    unittest.main()