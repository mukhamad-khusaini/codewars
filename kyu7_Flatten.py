def flatten(lst):
    arr = []
    for i in lst:
        if type(i)==type([]):
            for x in i:
                arr.append(x)
        else:
            arr.append(i)
    
    return arr

print(flatten(['M', -4, [20, 2, -3], 'L', 18, 1, 0.49704046603560315, -10.971917332404665, [-9, 2], 5]))
# print(type())