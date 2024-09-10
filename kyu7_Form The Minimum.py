def min_value(digits):
    so=sorted(digits)
    mark=[]
    for i in so:
        if mark==[]: mark.append(i)
        if mark[-1]==i: continue
        mark.append(i)
        
    return int("".join(str(i) for i in mark))

print(min_value({4,7,1,3}))