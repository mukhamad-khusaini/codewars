def explode(s):
    return "".join([i*int(i) for i in s])


print(explode("123"))