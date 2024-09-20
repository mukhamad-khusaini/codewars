def div_con(x):
    # your code here
    return sum([i for i in x if type(i)==type(1)]) - sum([int(i) for i in x if type(i)==type("s")])