import unittest

from src.SimpleFun180GradRotated import rotate_paper

class TestSimpleFun180GradRotated(unittest.TestCase):
    
    def test_mehere_Zeichen(self):
        self.assertEqual(rotate_paper("1337"), False)
        
    def test_leer(self):
        self.assertEqual(rotate_paper(""), True)
        
    def test_wenn_null(self):
        self.assertEqual(rotate_paper("0"), True)
        
    def test_wenn_even_zeichen(self):
        self.assertEqual(rotate_paper("22"), True)
        
if __name__ == "__main__":
    unittest.main()