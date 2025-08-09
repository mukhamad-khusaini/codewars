def bingo(array): 
    return "LOSE" if False in [True if i in array else False for i in [2,9,14,7,15]] else "WIN"