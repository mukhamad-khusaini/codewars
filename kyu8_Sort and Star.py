def two_sort(array):
    def fun(i):
        return [ord(li) for li in i]
    vin=sorted(list(map(fun, array)))

    return "***".join([chr(i) for i in vin[0]])

print(two_sort(["turns", "out", "random", "test", "cases", "are", "abe", "than", "writing", "out", "basic", "ones"]))