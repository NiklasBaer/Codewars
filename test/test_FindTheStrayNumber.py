import unittest

from src.FindTheStrayNumber import stray

class TestFindTheStrayNumber(unittest.TestCase):
    
    def test_viele_zahlen(self):
        self.assertEqual(stray([1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1]),3)
    
    def test_wenn_unternull(self):
        self.assertEqual(stray([-1,-1,-1,-1,-1,-35]), -35)
        
    def test_wenn_gemischt(self):
        self.assertEqual(stray([-1,-1,-1,3,3,3,3]), 3)
        
        
        
if __name__ == "__main__" :
    unittest.main()