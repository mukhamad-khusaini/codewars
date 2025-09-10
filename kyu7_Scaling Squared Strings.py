def scale(strng, k, v):
    if not strng: return ""
    ns=strng.split("\n")
    kh=[]
    for i in ns:
        temp=[]
        for x in i:
            temp.append(x*k)
        kh.append("".join(temp))

    vv=[]
    for i in kh:
        vv.append("\n".join([i for x in range(v)]))
  
    return "\n".join(vv)

print(scale("abcd\nefgh\nijkl\nmnop", 2,3))