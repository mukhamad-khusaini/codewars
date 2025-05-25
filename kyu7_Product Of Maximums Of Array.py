def max_product(lst, n_largest_elements):
    t=sorted(lst, reverse=True)[:n_largest_elements]
    res=1
    for i in t:
        res=res*i
    return res

print(max_product([1,4,2,5,7,4,1,6,9],2))