def multiplication_table(size):
    col = list(range(1, size+1))
    stnd=[col]
    for i in range(1,size):
        stnd.append([col[i]] + [col[i]*col[x] for x in range(1, size)])
    
    return stnd

print(multiplication_table(5))