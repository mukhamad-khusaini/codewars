def ordered_count(inp):
    li=[(i, inp.count(i)) for i in inp]
    r=[]
    for i in li:
        if i in r:
            continue
        r.append(i)

    return r

print(ordered_count("abracadabra"))
