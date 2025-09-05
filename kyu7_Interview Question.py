def get_strings(city):
    uniqq=[]
    for i in city.lower().replace(" ",""):
        if i in uniqq: continue
        uniqq.append(i)
    return ",".join([ uniqq[i] + ":" + city.lower().count(uniqq[i])*"*" for i in range(len(uniqq))])

print(get_strings("Chicago offer"))