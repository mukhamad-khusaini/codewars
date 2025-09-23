def partlist(arr):
    res=[]
    for i in range(1,len(arr)):
        res.append((" ".join(arr[:i])," ".join(arr[i:])))
    
    return res

print(partlist(["1", "2", "3","4","5"]))
# print([1,2,3,4,5][:])