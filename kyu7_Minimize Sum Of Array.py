def min_sum(arr):
    temp=arr
    sumer=[]
    while len(temp)>0:
        maxi=max(temp)
        temp.pop(temp.index(max(temp)))
        mini=min(temp)
        temp.pop(temp.index(min(temp)))
        sumer.append(maxi*mini)
    return sum(sumer)

print(min_sum([12,6,10,26,3,24]))