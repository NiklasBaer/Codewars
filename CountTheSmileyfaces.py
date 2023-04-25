def Count_smileys(arr):
    Count = 0
    for Smiley in arr:
        print(Smiley)
        HatAugen = ":" in Smiley or ";" in Smiley
        print(HatAugen)
        HatMund = ")" in Smiley or "(" in Smiley or "D" in Smiley
        print(HatMund)
        if HatMund == True and HatAugen == True:
            Count = Count + 1
        print(Count)
    return Count



Count_smileys([':D',':~)',';~D',';)'])
