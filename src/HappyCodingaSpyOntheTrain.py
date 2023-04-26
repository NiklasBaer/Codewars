def length_of_railway(sounds):
    #Banhof = Rein or Raus 呜呜呜
    #Auf_Schiene = 10 or 20 哐当
    Geräusche = list(sounds)
    Anfang = list(sounds)
    if sounds == [] or sounds == "":
        return[]
    print(Geräusche)
    Geschwindigkeit = 0
    Im_Bahnhof = True
    Bahnhoferstemal = 0
    Anfang = Anfang.pop(0)
    if Anfang == "哐" :
        Geschwindigkeit = 0
        return Geschwindigkeit
    
    for GeräuschIndex in range(len(Geräusche)):
        teil_von_Geräusche = Geräusche[GeräuschIndex]
        
        if teil_von_Geräusche == "呜":
            Bahnhoferstemal = Bahnhoferstemal + 1
            
            Im_Bahnhof = not True
            if Bahnhoferstemal == 6:
                Im_Bahnhof = not False
                Bahnhoferstemal = 0
        elif teil_von_Geräusche == "哐":
        

            if Im_Bahnhof == False:
                Geschwindigkeit = Geschwindigkeit + 20
            elif Im_Bahnhof == True:
               Geschwindigkeit = Geschwindigkeit +10
            else:
                pass                
                
        
    return Geschwindigkeit
        
