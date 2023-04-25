import unittest

from src.HappyCodingaSpyOntheTrain import length_of_railway

class TestHappyCodingaSpyOnTheTrain(unittest.TestCase):
    
    def test_wenn_leer(sefl):
        sefl.assertEqual(length_of_railway(""), [])
        sefl.assertEqual(length_of_railway([]), [])
        
    def test_wenn_nur_Bahnhof(self):
        self.assertEqual(length_of_railway("呜呜呜"), 0)
        
    def test_wenn_nur_Strecke(self):
        self.assertEqual(length_of_railway("哐当"),0)
        
    def test_wenn_nur_Bahnhof(self):
        self.assertEqual(length_of_railway("呜呜呜呜呜呜"), 0)
    
    def test_wenn_nur_Strecke(self):
        self.assertEqual(length_of_railway("哐当哐当哐当"), 0)
        
    def test_wenn_lange_Strecke(self):
        self.assertEqual(length_of_railway("呜呜呜哐当哐当哐当哐当哐当哐当哐当哐当哐当哐当呜呜呜哐当呜呜呜"), 210)
        
        
        
        
if __name__ == "__main__" :
    unittest.main()