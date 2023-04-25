import unittest

from src.FindTheStrayNumber import stray

class TestFindTheStrayNumber(unittest.TestCase):
    
    def viele_zahlen(self):
        self.assertEqual(stray([1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1]),3)
        
        
        
if __name__ == "__main__" :
    unittest.main()