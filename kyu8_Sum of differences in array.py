def sum_of_differences(arr):
    if len(arr)==0: return 0
    c=sorted(arr,reverse=True)
    inc=[]
    for i in range(len(c)):
        if i==len(c)-1: return sum(inc)
        inc.append(c[i]-c[i+1])

print(sum_of_differences([1,2,10]))
        