def nb_dig(n, d):
    num=[str(i**2) for i in range(0,n+1)]
    return "".join(num).count(str(d))

print(nb_dig(5750,0))
# print(["1" in x for x in [str(i**2) for i in list(range(0,11))]])
# print(list(range(0,5751)))
print(str(0) in str(5750**2))