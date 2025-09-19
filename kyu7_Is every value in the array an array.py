def arr_check(arr):
    return all(type(i) == type([]) for i in arr)

print(arr_check([[],[11,2]]))