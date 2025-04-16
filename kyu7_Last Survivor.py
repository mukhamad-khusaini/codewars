def last_survivor(letters, coords): 
    str_arr=list(letters)
    for s in coords:
        str_arr=[str_arr[i] for i in range(len(str_arr)) if i!=s]
    
    return "".join(str_arr)