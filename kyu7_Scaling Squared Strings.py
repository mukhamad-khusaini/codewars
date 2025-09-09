def scale(strng, k, v):
    ns=strng.split("\n")
    kh=[]
    for i in ns:
        temp=[]
        for x in i:
            temp.append(x*k)
        kh.append("".join(temp))
    
    vv=[]
    for i in kh:
        vv.append(i*v)
    
    return "\n".join(vv)

print(scale("abcd\nefgh\nijkl\nmnop", 2,3))