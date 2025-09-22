def consecutive(arr):
    if not arr: return 0
    orde=sorted(arr)
    chk=orde[0]
    min=[]
    for i in range(1,len(orde)):
        min+=[i for i in range(chk+1,orde[i])]
        chk=orde[i]
    
    return len(min)

print(consecutive([1,5,100,7]))