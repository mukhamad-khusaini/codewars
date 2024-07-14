def correct(s):
    a=[]
    for i in s:
        if i=="1": a.append("I")
        elif i=="5": a.append("S")
        elif i=="0": a.append("O")
        else: a.append(i)
        
    return "".join(a)