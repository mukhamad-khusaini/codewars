def logical_calc(array, op):
    global c
    c=True
    if op=="AND":
        for i in range(len(array)):
            if i == 0:
                c=array[i]
            else:
                c=c and array[i]
        return c
    elif op=="OR":
        for i in range(len(array)):
            if i == 0:
                c=array[i]
            else:
                c=c or array[i]
        return c
    else:
        for i in range(len(array)):
            if i == 0:
                c=array[i]
            else:
                c=(c==True and array[i]==False) or (c==False and array[i]==True)
        return c
