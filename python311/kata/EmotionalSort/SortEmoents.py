def sort_emotions(arr, order):
    # Schauen welche zeichen drinne sind
    # Schauen ob man es von gut nach schlecht machen soll oder von schlecht nach gut
    # Liste weider zsm stellen und rausgeben
    Simile = Codirer(arr, order)
    SimileCodeer = Simile.Verarbeitung()
    return SimileCodeer


class Codirer():

    def __init__(self, input, order) -> None:
        self.SmilieLIste = input
        self.Smilieorder = order

    def DictonarySmylie(self, arr):

        Smilie = {
            ":D": 1,
            ":)": 2,
            ":|": 3,
            ":(": 4,
            "T_T": 5
        }

        return Smilie[arr]

    def DictonarySmylieCode(self, Verarbeitet):

        SmilieCodiert = {
            1: ":D",
            2: ":)",
            3: ":|",
            4: ":(",
            5: "T_T"
        }

        return SmilieCodiert[Verarbeitet]

    def Verarbeitung(self):
        Zwichenliste = map(self.DictonarySmylie, self.SmilieLIste)
        MapVerarbeiteteListe = list(Zwichenliste)
        print(MapVerarbeiteteListe)
        MapVerarbeiteteListe.sort()
        print(MapVerarbeiteteListe)
        if self.Smilieorder == True:
            abfrageTrue = map(self.DictonarySmylieCode, MapVerarbeiteteListe)
            ErgbenisTrue = list(abfrageTrue)
            return ErgbenisTrue

        if self.Smilieorder == False:
            MapVerarbeiteteListe.sort(reverse=True)
            abfrageFalse = map(self.DictonarySmylieCode, MapVerarbeiteteListe)
            ErgbenisFalse = list(abfrageFalse)
            return ErgbenisFalse


sort_emotions([':D', 'T_T', ':D', ':('], True)
