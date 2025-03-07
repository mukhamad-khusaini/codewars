def flatten_and_sort(arr):
    a=[]
    [[a.append(x) for x in i] for i in arr]
    return sorted(a)