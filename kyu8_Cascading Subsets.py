def each_cons(lst, n):
    lss=[]
    for i in range(len(lst)):
        if len(lst)-i-n<0: break
        tmp=[]
        for x in range(n):
            tmp.append(lst[i+x])

        lss.append(tmp)
    
    return lss

print(each_cons([1,2,3,4,5,6,7,8],3))