def _all(seq, fun): 
    return False if False in [fun(i) for i in seq] else True