def count_smileys(arr):
    Count = 0
    for Smiley in arr:
        print(Smiley)
        if len(Smiley) == 2:
            HatAugen = ":" in Smiley or ";" in Smiley
            print(HatAugen)
            HatMund = ")" in Smiley or "D" in Smiley
            print(HatMund)
            if HatMund == True and HatAugen == True:
                Count = Count + 1
        print(Count)
        if len(Smiley) == 3:
            HatAugen = ":" in Smiley or ";" in Smiley
            HatMund = ")" in Smiley or "D" in Smiley
            HatNase = "-" in Smiley or "~" in Smiley
            if HatAugen == True and HatMund == True and HatNase == True:
                Count = Count + 1
        
    return Count



count_smileys([':)',':(',':D',':O',':;'])
count_smileys([";o)"])
