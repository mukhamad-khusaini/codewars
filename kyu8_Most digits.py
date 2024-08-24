def find_longest(arr):
    return arr[[len(str(i)) for i in arr].index(max([len(str(i)) for i in arr]))]

print(find_longest([12,222,11111, 22222]))