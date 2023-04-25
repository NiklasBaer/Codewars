import unittest

from src.AllStarCodeChallenge import rotate

class TestAllStarCodeChallenge(unittest.TestCase):
    
    def test_wenn_leer(self):
        self.assertEqual(rotate([]), [])
        
    def test_wenn_zahlen(self):
        self.assertEqual(rotate("124"), ["241", "412", "124"])
        
        
        
        
if __name__ == "__main__":
    unittest.main()
    
