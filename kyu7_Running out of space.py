def spacey(array):
    return ["".join([array[x] for x in range(i)]) for i in range(len(array)+1)][1:]

print(spacey(["i", "have", "no", "spaced"]))