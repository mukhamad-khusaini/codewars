def beggars(values, n):
    if n==0: return []
    distItem=[[0] for i in range(n)]
    for i in range(len(values)):
        distItem[i%n].append(values[i])
    
    return [sum(i) for i in distItem]
print(beggars([1,2,3,4,5,5],10))