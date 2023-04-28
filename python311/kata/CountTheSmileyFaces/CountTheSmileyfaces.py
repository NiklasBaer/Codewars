def count_smileys(arr):
    Count = 0
    for Smiley in arr:
        if len(Smiley) == 2:
            HatAugen = ":" in Smiley or ";" in Smiley
            HatMund = ")" in Smiley or "D" in Smiley
            if HatMund == True and HatAugen == True:
                Count = Count + 1
        if len(Smiley) == 3:
            HatAugen = ":" in Smiley or ";" in Smiley
            HatMund = ")" in Smiley or "D" in Smiley
            HatNase = "-" in Smiley or "~" in Smiley
            if HatAugen == True and HatMund == True and HatNase == True:
                Count = Count + 1
        
    return Count

