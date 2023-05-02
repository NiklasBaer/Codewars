import unittest

from Beeramid import beeramid

class TestBeeramid(unittest.TestCase):

    def test_wenn_null(self):
        self.assertEqual(beeramid(0, 0), "")
        self.assertEqual(beeramid(1000, 0), "")
        
    def test_wenn_beides_geben(self):
        self.assertEqual(beeramid(1500, 2), 12)
        self.assertEqual(beeramid(5000, 3), 16)
        self.assertEqual(beeramid(9, 2), 1)
        self.assertEqual(beeramid(-1, 4), 0)
    
    def test_wenn_ungerade(self):
        self.assertEqual(beeramid(21, 1.5), 3)
        
        
if __name__ == "__main__":
    unittest.main()