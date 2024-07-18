def remove_smallest(numbers):
    n=list(numbers)
    if(len(n)==0): return []
    n.pop(n.index(min(n)))
    return n


print(remove_smallest([5,2,3,4,5,6]))