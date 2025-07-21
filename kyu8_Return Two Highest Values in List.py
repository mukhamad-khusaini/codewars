def two_highest(arg1):
    return sorted(list(set(arg1)))[::-1][:2]

print(two_highest([1,2,3,2,4,5,5,3]))