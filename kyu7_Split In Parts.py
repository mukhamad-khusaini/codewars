def split_in_parts(s, part_length): 
    sl=s
    res=[]
    while len(sl)>0:
        if len(sl)<=part_length: 
            res.append(sl)
            sl=[]
        else:
            res.append(sl[:part_length])
            sl=sl[part_length:]
    
    return " ".join(res)

print(split_in_parts("ayta",1))