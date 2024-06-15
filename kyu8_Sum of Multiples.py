def sum_mul(n, m):
    if(n==0 or m==0 or n<0 or m<0): return "INVALID"
    elif(n>m): return 0
    num=0
    for i in range(m):
        if((i+1)*n >= m): return num
        num+=(i+1)*n

print(sum_mul(4,-7))