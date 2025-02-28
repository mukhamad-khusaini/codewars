def fold_to(distance):
    if distance < 0: return None
    i=0.0001
    fold=0
    while i<distance:
        i*=2
        fold+=1
    return fold