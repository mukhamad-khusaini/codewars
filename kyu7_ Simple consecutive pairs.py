def pairs(arr):
    newOne=[]
    while arr:
        newOne.append(arr[:2])
        arr=arr[2:]
    
    return sum([1 if abs(i[0]-i[1])==1 else 0 for i in newOne if len(i)==2])

print(pairs([1,2,3,4,5,6,7,8,9]))