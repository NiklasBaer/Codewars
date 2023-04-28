from src.SchauenWelcheDrinne import SchauenWelcheDrinnen
from src.SchauenWelcheDrinne import SchauenInWelcheRichtung
from src.SchauenWelcheDrinne import Ergebnis

def sort_emotions(arr, order):
    #Schauen welche zeichen drinne sind
    #Schauen ob man es von gut nach schlecht machen soll oder von schlecht nach gut
    #Liste weider zsm stellen und rausgeben
    
    Welche_drinne = SchauenWelcheDrinnen(arr)
    WieVieleWelche = Welche_drinne.Schauenwelchedrinne()
        
    Welche_Richtung = SchauenInWelcheRichtung(order)
    WelcheRichtung = Welche_Richtung.SchauenWelcheRichtung
    
    ZwischenErgebnis = Ergebnis(WieVieleWelche, Welche_Richtung)
    Result = ZwischenErgebnis.Lösung()
    
    #Die KLssen sind so weit fertig muss nur noch an der Lösung gebastelt werden und ein paar bugfixes gemacht werden alles funktioniert so bis auf die einen Unittest 
    
sort_emotions([ ':D', 'T_T', ':D', ':(' ], True)

