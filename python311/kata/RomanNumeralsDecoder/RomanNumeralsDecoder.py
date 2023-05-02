def solution(roman):
    Zahljanein = roman.isdigit()
    if roman == "" or roman == []:
        return roman
    if Zahljanein:
        return ""
    if "-" in roman:
        return ""
    Roman = VerarbeitungRoman(roman)
    VerarbeiteteRomanZahl = Roman.Verarbeitung()
    return VerarbeiteteRomanZahl


class VerarbeitungRoman():

    def __init__(self, input) -> None:
        self.RomanZahl = input

    def Symbloliste(self, zeichen):

        SymbolList = {
            "I":    1,
            "V":    5,
            "X":    10,
            "L":    50,
            "C":    100,
            "D":    500,
            "M":    1000,
            "ↁ":    5000,
            "ↂ":   10000,
            "ↇ":    50000,
            "ↈ":   100000
        }
        return SymbolList[zeichen]

    def Verarbeitung(self):
        ZwischenRausgesuchteZahl = map(self.Symbloliste, self.RomanZahl)

        RausgesuchteZahl = list(ZwischenRausgesuchteZahl)

        InputList = list(self.RomanZahl)

        UmgedrehteListe = RausgesuchteZahl[::-1]
        letzerWert = 0
        carry = 0
        for JedenIndex in UmgedrehteListe:

            if JedenIndex >= letzerWert:
                carry = carry + JedenIndex
                letzerWert = JedenIndex
            else:
                carry = carry - JedenIndex

        return carry
