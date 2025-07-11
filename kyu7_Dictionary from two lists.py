def create_dict(keys, values):
    res={}
    for i,x in zip(keys, range(len(keys))):
        try:
            res[i]=values[x]
        except:
            res[i]=None
    
    return res
        
print(create_dict(["a","b","c","d"],[1,2,3]))