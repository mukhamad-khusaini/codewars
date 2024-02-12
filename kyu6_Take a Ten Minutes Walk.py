def is_valid_walk(walk):
    l={
        "n": 0,
        "s": 0,
        "w": 0,
        "e": 0,
    }

    for i in walk:
        if(i=="n"):
            l["n"]+=1
        elif(i=="s"):
            l["s"]+=1
        elif(i=="w"):
            l["w"]+=1
        elif(i=="e"):
            l["e"]+=1

    return (sum(l.values()) == 10 and l['n']-l['s']==0 and l['w']-l['e']==0 )

print(is_valid_walk(['n','n','s','w','e']))
        