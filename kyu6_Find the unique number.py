def find_uniq(arr):
    whole=list(set(arr))
    for i in whole:
        if arr.count(i)==1: return i

print(find_uniq([1,1,1,3,5,6,5,6]))