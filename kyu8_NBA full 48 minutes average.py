def nba_extrap(ppg, mpg):
    if mpg==0: return 0
    return  float(f"{ppg/(mpg/48):.1f}")