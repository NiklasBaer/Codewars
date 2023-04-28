import unittest

from python311.kata.RmoveStringSpaces.RemoveStringSpaces import no_space

class TestRemoveStringsSpaces(unittest.TestCase):
    
    def test_langerText(self):
        self.assertEqual(no_space("Ich habe keine Ahnung was ich hier rein schreiben soll ich weiß nur das ich gerade irgend ein mist schreibe und es sich gerade irgendwer durchließt"), "IchhabekeineAhnungwasichhierreinschreibensollichweißnurdasichgeradeirgendeinmistschreibeundessichgeradeirgendwerdurchließt")
        
    def test_langeLeerzeichen(self):
        self.assertEqual(no_space("Warum       mache       ich     das    hier   "), "Warummacheichdashier") 
           
if __name__ == "__main__" :
    unittest.main()