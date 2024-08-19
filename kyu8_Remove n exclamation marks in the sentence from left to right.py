def remove(st, n):
    if st == "": return ""
    num=n
    arr = []
    for i in st:
        if i=="!":
            if num>0:
                num-=1
                continue
            else: arr.append(i)
        else:
            arr.append(i)
    
    return "".join(arr)


print(remove("!sada!",1))