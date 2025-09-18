def cube_odd(arr):
    if type("s") in [type(i) for i in arr] or type(True) in [type(i) for i in arr]: return None
    return sum([i**3 for i in arr if i%2!=0])