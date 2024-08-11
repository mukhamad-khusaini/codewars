def multiply(n):
    return n * (5**len([i for i in str(n).split("-") if i!=""][0]))

print(multiply(-2))