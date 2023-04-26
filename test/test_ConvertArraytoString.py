import unittest

from src.ConvertArraytoString import to_float_array

class TestConvertArraytoString(unittest.TestCase):
    
    def test_wenn_leer(self):
        self.assertEqual(to_float_array(""), [])
        
    def test_wenn_null(self):
        self.assertEqual(to_float_array("0"), [0])
        
    def test_wenn_lang(self):
        self.assertEqual(to_float_array(["12","2","3"]), [12, 2, 3])
        
        
        
        
if __name__ == "__main__":
    unittest.main()