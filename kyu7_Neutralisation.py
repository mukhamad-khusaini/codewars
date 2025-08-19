def neutralise(s1, s2):
    return "".join(["+" if (i=="+" and x=="+") or (x=="+" and i=="+") else "-" if (i=="-" and x=="-") or (x=="-" and i=="-") else "0" for i,x in zip(s1,s2)])