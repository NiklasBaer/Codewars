
class SchauenWelcheDrinnen():
    
    def __init__(self,input) -> None:
        self.ListeInput = input
    
    def Schauenwelchedrinne(self):
        ZwischenListe = []
        WieViele = []
        return self.ListeInput
        
            
        
class SchauenInWelcheRichtung():
    
    def __init__(self, input) -> None:
        self.RichtungInput = input
        self.Richtung = 0
        self.Result = []
        
        
    def SchauenWelcheRichtung(self):
        if self.RichtungInput == True:
            self.Richtung = self.Richtung + 1
            return self.Richtung
        elif self.Richtung == False:
            self.Richtung = self.Richtung - 1
            return self.Richtung
        
        

class Ergebnis():
    
    def __init__(self,WelcheDrin,WelcheRichtung) -> None:
        self.Richtung = WelcheRichtung
        self.Drin= WelcheDrin
        self.Finish = [""]
            
            
    def Lösung(self):
        ärsezten = str(self.Drin).replace(":D", "1") 
        ärsezten = str(self.Drin).replace("T_T", "1")
        return ärsezten
            
        pass
        
        
