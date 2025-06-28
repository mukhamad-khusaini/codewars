def compare(s1, s2):
    v1=0
    v2=0
    num=[str(i) for i in range(10)]
    if s1!=0 and s1!=None:
        for i in s1.upper():
            if i in num:
                v1=0
                break
            v1+=ord(i)
    if s2!=0 and s2!=None:
        for i in s2.upper():
            if i in num:
                v2=0
                break
            v2+=ord(i)
    
    return v1==v2



print([1,2,3]+[5,6,7])