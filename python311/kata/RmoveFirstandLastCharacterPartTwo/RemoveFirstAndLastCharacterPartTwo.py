def array(strng):
    seqs = strng.split(",")
    
    if len(seqs) <= 2:
        return None
    
    new_strng = " ".join(seqs[1:-1])
    
    return new_strng
