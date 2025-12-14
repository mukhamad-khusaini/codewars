def up_array(arr):
    if not arr or True in [True for i in arr if i<0 or i>9]:
        return None
    elif len(arr)==1: return [int(i) for i in list(str(arr[0]+1))]
    
    zero=0
    for i in arr:
        if i == 0: zero+=1
        else: break
    
    return [0 for i in range(zero)] + [int(x) for x in list(str(int("".join([str(i) for i in arr]))+1))]
    
print(up_array([0,0,0,0,2,3,4,9]))