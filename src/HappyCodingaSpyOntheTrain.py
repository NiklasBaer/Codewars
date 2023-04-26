def length_of_railway(sounds):
    PfeifenTon = "呜"
    StreckenTon = "哐"
    #Banhof = Rein or Raus 呜呜呜
    #Auf_Schiene = 10 or 20 哐当
    Geräusche = list(sounds)
    
    
    if sounds == [] or sounds == "":
        
        return[]
    
    Anfang = Geräusche[0]
    
    Strecke = 0
    
    if Anfang == PfeifenTon:
        
        Im_Bahnhof = True
        
    else:
        Im_Bahnhof = False
    
    if Anfang == StreckenTon :
        
        Strecke = 0
        
        return Strecke
    
    for GeräuschIndex in range(len(Geräusche)):
        
        AktuellerTon = Geräusche[GeräuschIndex]
        
        if AktuellerTon == PfeifenTon:
            
            Im_Bahnhof = not Im_Bahnhof
            
           
        elif AktuellerTon == StreckenTon:
        

            if Im_Bahnhof == True:
                
                Strecke = Strecke + 10
                
            elif Im_Bahnhof == False:
                
               Strecke = Strecke + 20
                          
                
        
    return Strecke 
        
