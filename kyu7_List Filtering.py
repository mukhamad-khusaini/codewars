def filter_list(l):
    return [i for i in l if type(i)==int]
        

print(filter_list(["a",2,"vs",2,12,6]))