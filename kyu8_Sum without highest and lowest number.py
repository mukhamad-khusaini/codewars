def sum_array(arr):
    return sum(arr) - (min(arr) + max(arr)) if(arr and len(arr)>2) else 0


print(sum_array([1,1,2,3,4]))