import unittest

from python311.kata.SimpleFun156RotatePaperby180Degrees.StringUmdreher import StringUmdreher


class TestStringUmdreher(unittest.TestCase):

    def test_instanziirung(self):
        x = StringUmdreher("Test")

    def test_leeren_string(self):
        x = StringUmdreher("")
        y = x.drehe_um()
        self.assertEqual(y, "")

    def test_mit_zwei_zeichen(self):
        x = StringUmdreher("AB")
        y = x.drehe_um()
        self.assertEqual(y, "BA")

    def test_langer_String(self):
        x = StringUmdreher("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        y = x.drehe_um()
        self.assertEqual(y, "ZYXWVUTSRQPONMLKJIHGFEDCBA")


if __name__ == "__main__":
    unittest.main()
