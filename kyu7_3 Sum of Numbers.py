def get_sum(a,b):
    l=[a,b]
    l.sort()
    return sum([i for i in range(l[0],l[1]+1)])

print(get_sum(4,-4))