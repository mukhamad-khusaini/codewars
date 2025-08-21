def consecutive(arr, a, b):
    return f"{a} {b}" in " ".join([str(i) for i in arr]) or f"{b} {a}" in " ".join([str(i) for i in arr])

print(consecutive([1,2,3,4,5,6],6,3))