def Liste_Bereitstellen(equation):
    equation = equation
    Liste_ohen_Leerzeichen = "".join(equation.split())
    moded_List = Liste_ohen_Leerzeichen.replace("@", "")
    Prüfen_Plus_Minus(moded_List)
    
def Prüfen_Plus_Minus(moded_List):
    print(moded_List)
    



def evaluate(moded_List):
    pass


Liste_Bereitstellen("1 @ 1")