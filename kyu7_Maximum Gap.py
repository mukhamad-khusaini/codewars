def max_gap(numbers):
    lss=sorted(numbers)
    res=[]
    for i in range(len(lss)):
        if len(lss)-i-2<0: break
        tmp=[]
        for x in range(2):
            tmp.append(lss[i+x])

        res.append(tmp)
    
    return max([abs(i[0]-i[1]) for i in res])

print(max_gap([13,10,2,9,5]))