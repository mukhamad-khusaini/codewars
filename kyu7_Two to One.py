def longest(a1, a2):
    list=a1+a2
    dicts={}
    cont=[]

    for i in range(len(list)):
        if(list[i] in dicts):
            dicts[list[i]].append(list[i])
        else:
            dicts.update({list[i]:[list[i]]})
    
    for i in dicts.keys():
        cont.append(i)
    
    return "".join(sorted(cont))

print(longest("asavvasvasd","sarqwzgfsd"))


