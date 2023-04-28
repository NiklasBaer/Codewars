import unittest

from python311.kata.RmoveFirstandLastCharacterPartTwo.RemoveFirstAndLastCharacterPartTwo import array

class TestRemoveCharacterPartTwo(unittest.TestCase):
    
    def test_wenn_leer(self):
        self.assertEqual(array(""), None)
        
        
    def test_wenn_kürzer_als2(self):
        self.assertEqual(array("1,2"), None)
    
    def test_wenn_buschtaben(self):
        self.assertEqual(array("ab ,rerz ,asg"), "rerz ")
        
if __name__ == "__main__":
    unittest.main()