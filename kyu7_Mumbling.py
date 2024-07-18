def accum(st):
    l=[]
    i=0
    while i < len(st):
        for x in range(i+1):
            if x == 0: l.append(st[i].upper())
            else: l.append(st[i].lower())
        
        if i+1 != len(st): l.append("-")
        i+=1
    
    return "".join(l)

print(accum("Senyorr"))