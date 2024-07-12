def first_non_consecutive(arr):
    for i in range(len(arr)):
        if i == 0: continue
        elif arr[i]!=arr[i-1]+1: return arr[i]
        elif i==len(arr)-1: return None
        
        
print(first_non_consecutive([4,5,6,7,8,9,11]))