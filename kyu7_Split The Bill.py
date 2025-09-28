def split_the_bill(x):
    mean = sum([i for i in x.values()])/len(x.keys())
    res={}
    for i in x.keys():
        res[i]=round(x[i]-mean,2)

    return res

print(split_the_bill({"ani": 20, "ari": 70, "beti": 2}))