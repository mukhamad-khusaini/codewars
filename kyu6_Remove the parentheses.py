def remove_parentheses(st):
    delete=[]
    currentPare=[]
    rejector=0
    for i in range(len(st)):
        if st[i]=="(":
            if currentPare:
                currentPare.append(i)
                rejector+=1
            else:
                currentPare.append(i)
        elif st[i]==")":
            if rejector!=0:
                rejector-=1
                currentPare.append(i)
            else:
                currentPare.append(i)
                delete+=list(range(currentPare[0],currentPare[-1]+1))
                currentPare=[]
    
    return "".join([st[i] for i in range(len(st)) if i not in delete])

print(remove_parentheses("(tanya) (jawab) (saja) (hai(hai))f"))