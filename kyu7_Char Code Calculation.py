def calc(x):
    # your code here
    T="".join([str(ord(i)) for i in x])
    return sum([int(i) for i in T])-sum([int(i) for i in "".join(["1" if i=="7" else i for i in T])])

print(calc("abcdef"))