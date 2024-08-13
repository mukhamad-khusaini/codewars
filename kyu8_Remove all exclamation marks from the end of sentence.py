def remove(st):
    str=[]
    for i in range(len(st)):
        if i==len(st)-1 and st[i]!="!": 
            str.append(st[i])
            return "".join(str)
        elif (st[i]=="!"):
            for x in range(len(st[i:])):
                if st[i:][x]!="!":
                    str.append(st[i:][0])
                    break
                elif x==len(st[i:])-1:
                    return "".join(str)
        else: str.append(st[i])



print(remove("Hai!!!!!j!!"))

# print("Hai!"[3:])