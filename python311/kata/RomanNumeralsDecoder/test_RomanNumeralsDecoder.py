import unittest

from python311.kata.RomanNumeralsDecoder.RomanNumeralsDecoder import solution
from python311.kata.RomanNumeralsDecoder.RomanNumeralsDecoder import VerarbeitungRoman


class TestRomanNumeralsDecoder(unittest.TestCase):

    def test_wenn_leer(self):
        self.assertEqual(solution(""), "")

    def test_inizaliizieren(self):
        x = VerarbeitungRoman("")

    def test_wenn_null_normaleZahlen(self):
        self.assertEqual(solution("0"), "")
        self.assertEqual(solution("20"), "")
        self.assertEqual(solution("3457"), "")
        self.assertEqual(solution("1"), "")
        self.assertEqual(solution("2350"), "")
        self.assertEqual(solution("986235"), "")

    def test_minus_zahlen(self):
        self.assertEqual(solution("-1"), "")
        self.assertEqual(solution("-34657"), "")

    def test_einzelne_RomaZeichen(self):
        self.assertEqual(solution("I"), 1)
        self.assertEqual(solution("V"), 5)
        self.assertEqual(solution("X"), 10)
        self.assertEqual(solution("L"), 50)
        self.assertEqual(solution("C"), 100)
        self.assertEqual(solution("D"), 500)
        self.assertEqual(solution("M"), 1000)

    def test_ander_zeichen(self):
        self.assertEqual(solution("ↁ"), 5000)
        self.assertEqual(solution("ↂ"), 10000)
        self.assertEqual(solution("ↇ"), 50000)
        self.assertEqual(solution("ↈ"), 100000)

    def test_leichte_kombinationen(self):
        self.assertEqual(solution("II"), 2)
        self.assertEqual(solution("IV"), 4)
        self.assertEqual(solution("VI"), 6)
        self.assertEqual(solution("VII"), 7)
        self.assertEqual(solution("IX"), 9)
        self.assertEqual(solution("XI"), 11)
        self.assertEqual(solution("XII"), 12)
        self.assertEqual(solution("XIV"), 14)
        self.assertEqual(solution("XV"), 15)
        self.assertEqual(solution("XVI"), 16)

    def test_normal_kombinationen(self):
        self.assertEqual(solution("MMXVI"), 2016)
        self.assertEqual(solution("XVI"), 16)
        self.assertEqual(solution("CXIV"), 114)
        self.assertEqual(solution("XLIII"), 43)
        self.assertEqual(solution("DCCXVIII"), 718)
        self.assertEqual(solution("XXXVII"), 37)
        self.assertEqual(solution("CLXIX"), 169)
        self.assertEqual(solution("XIV"), 14)
        self.assertEqual(solution("XXXIII"), 33)
        self.assertEqual(solution("CDLI"), 451)

    def test_schwere_kombinationen(self):
        self.assertEqual(solution("MDCCCXXV"), 1825)
        self.assertEqual(solution("MCMLXXXVI"), 1986)
        self.assertEqual(solution("MCMXXII"), 1922)
        self.assertEqual(solution("CCLXXXIII"), 283)
        self.assertEqual(solution("DCLXXIX"), 679)
        self.assertEqual(solution("MCCIII"), 1203)
        self.assertEqual(solution("CLXXXII"), 182)
        self.assertEqual(solution("MDCCXCVII"), 1797)
        self.assertEqual(solution("CLXXXIIMCMXXIIMCMLXXXVI"), 3682)
        self.assertEqual(solution("MCCXLIXMMCIX"), 2838)


if __name__ == "__main__":
    unittest.main()
