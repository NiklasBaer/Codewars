def infected_zeroes(lst):
    if lst == 0:
        return 0

    Zeros = Infected(lst)
    Ausgabe = Zeros.Infiziert()


class Infected():

    def __init__(self, input) -> None:
        self.Input = input
        self.Turns = 0

    def Schauen_wo_null(self):

        if 0 in self.Input:
            pass

        else:
            return "No value"

    def Infiziert(self):
        self.Input
        print(self.Input)

        sumInf = sum(self.Input)
        print(sumInf)

        while sumInf >= 2:

            a = int(list(self.Input[0]))
            b = int(list(self.Input[1]))

            zwischenergebnis = a + b

            self.Input = self.Input[2:]
            self.Input.insert(0, zwischenergebnis)

        print(self.Input)


infected_zeroes([0, 1, 1, 0])  # 1
