def friend(x):
    cont=[]
    for i in x:
        if(len(i)==4):
            cont.append(i)

    return cont

print(friend(["Mark", "josh", "gilbert", "madam", "Santi", "Yura", "matatabi"]))

