def dig_pow(n, p):
    digit=[int(x) for a,x in enumerate(str(n))]
    raised=0
    for i in range(len(digit)):
        raised += (digit[i]**(p+i))

    res=int(raised)/n
    
    if(res-int(res)==0):
        return int(res)

    return -1

print(dig_pow(4628, 3))