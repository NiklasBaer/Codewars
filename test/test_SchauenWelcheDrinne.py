import unittest

from src.SchauenWelcheDrinne import SchauenWelcheDrinnen
from src.SchauenWelcheDrinne import SchauenInWelcheRichtung
from src.SchauenWelcheDrinne import Ergebnis

class TestSchauenWelcheDrinne(unittest.TestCase):
    
    def test_instanziirung(self):
        x = SchauenWelcheDrinnen("Test")
    
    def test_wie_viele_drinnen(self):
        x = SchauenWelcheDrinnen([":("])
        y = x.Schauenwelchedrinne()
        self.assertEqual(y, [":("])
        
    def test_schauen_welche_Richtung(self):
        x = SchauenInWelcheRichtung(True)
        y = x.SchauenWelcheRichtung()
        self.assertEqual(y, 1)
        x = SchauenInWelcheRichtung(False)
        y = x.SchauenWelcheRichtung()
        self.assertEqual(y, -1)
        
    def test_kommt_alles_an(self):
        x = SchauenWelcheDrinnen([":D", ":D", ":D"])
        y = x.Schauenwelchedrinne()
        self.assertEqual(y,[":D",":D", ":D"])
        
    def test_wenn_unterschiedliche_Zeichen(self):
        x = SchauenWelcheDrinnen([ ':D', 'T_T', ':D', ':(' ])
        y = x.Schauenwelchedrinne()
        self.assertEqual(y,  [':D', 'T_T', ':D', ':('])    
        
    def test_ob_ankommt(self):
        x = Ergebnis([ ':D', 'T_T', ':D', ':(' ], True)
        y = x.Lösung()
        self.assertEqual(y,[])
if __name__ == "__main__" : 
    unittest.main() 