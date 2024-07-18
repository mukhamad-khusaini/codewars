def number(lines):
    return [f'{i+1}: {lines[i]}' for i in range(len(lines))]

print(number(["a", "b", "c"]))