def count_by(x, n):
    return [x+(x*i) for i in range(n)]
    
print(count_by(2,5))