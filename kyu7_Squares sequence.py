def squares(x, n):
    # ...
    if x<=0: return []
    l=[]
    for i in range(n):
        if i==0:
            l.append(x)
            continue
        else:
            l.append(l[i-1]**2)

    return l