def add(n):
    return lambda t: t+n

fst=add(2)

print(fst(3))