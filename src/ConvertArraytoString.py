def to_float_array(seq):
    if not seq:
        return []
    
    if '.' in seq[0]:
        cast_fn = float
    else:
        cast_fn = int
    
    cast_seq = list(map(cast_fn, seq))
    
    return cast_seq
