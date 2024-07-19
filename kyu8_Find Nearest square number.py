def nearest_sq(n):
    i=1
    while i**2<=n:
        if i**2==n: return n
        if (i+1)**2>n: break
        i+=1
    
    t=n-(i**2)
    k=((i+1)**2)-n
    
    if t<k: return i**2
    else: return (i+1)**2
    
print(nearest_sq(9999))