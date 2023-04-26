def evaluate(equation):
    Liste_ohne_Leerzeichen = "".join(equation.split())
    geteilt = Liste_ohne_Leerzeichen.split("@")
    return Rechnen(geteilt)
    
def Rechnen(moded_List):
    
    if moded_List == [""] or moded_List == "":
        return None
    
    if len(moded_List) < 2:
        return int(moded_List[0])
    
    # wiederhole solange liste mehr mindestens 2 Elemente enthält, mache
    while len(moded_List) >= 2:
        
        a = int(moded_List[0])
        b = int(moded_List[1])        
        
        if b == 0:
            return
        
        # * rechne( 1. Element, 2. Element)
        zwischenergebnis = (a + b) + (a - b) + (a * b) + (a // b)
        
        # * ersetze ersten 2 elemente mit ergebnis
        moded_List = moded_List[2:]
        moded_List.insert(0, zwischenergebnis)        
        
    ergebnis = moded_List[0]
    
    return ergebnis
    