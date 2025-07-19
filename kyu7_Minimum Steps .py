def minimum_steps(numbers, value):
    orr=sorted(numbers)
    v=0
    t=-1
    while v<value:
        t+=1
        if t==0:
            v+=orr[0]
        else:
            v+=orr[t]
        
    return t

print(minimum_steps([4,6,3],6))