import unittest

from python311.kata.CountTheSmileyFaces.CountTheSmileyfaces import count_smileys

class TestCountTheSmileyfaces(unittest.TestCase):

    def test_nur_auge_mund(self):
        self.assertEqual(count_smileys([";)", ":D"]), 2)
        
    def test_wenn_Leer(self):
        self.assertEqual(count_smileys([]),0)
        
    def test_wenn_alles(self):
        self.assertEqual(count_smileys([":-D", ";~)", ":-D"]), 3)        
        
    def test_nicht_alles_richtig(self):
        self.assertEqual(count_smileys([":+D", ";r)", ":-D", ";D", "igosdg"]), 2)
        
        
if __name__ == "__main__" :
    unittest.main()