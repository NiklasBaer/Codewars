from src.StringUmdreher import StringUmdreher
from src.ZeichenRotiere import ZeichenRotierer
def rotate_paper(number):
    if number == "" or number == []:
            return True
    
    Umdreher = StringUmdreher(number)
    UmgedrehteNummer = Umdreher.drehe_um()
    
    Rotierer = ZeichenRotierer(UmgedrehteNummer)
    RotierteNummer = Rotierer.Rotiere()
    numberls = list(number)
    
    if list(number) == RotierteNummer:
        
        return True
    else:
        return False
