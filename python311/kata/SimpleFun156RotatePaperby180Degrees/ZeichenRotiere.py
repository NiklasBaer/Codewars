class ZeichenRotierer():
    
    def __init__(self, input) -> None:
        self.Input = input
        
    def RotiereZeichen(self,zeichen):
        
        Zahlendrechung = {
            "1" : None, 
            "2" : "2",
            "3" : None,
            "4" : None,
            "5" : "5",
            "6" : "9",
            "7" : None,
            "8" : "8",
            "9" : "6",
            "0" : "0"
        }
        
        return Zahlendrechung[zeichen]
    
    def Rotiere(self):
        
        if self.Input == "" or self.Input == []:
            return self.Input
        
        
        
        ZwichenErgbins = map(self.RotiereZeichen, self.Input)
        Ergebnis = list(ZwichenErgbins)
        return Ergebnis
    
                
    
    