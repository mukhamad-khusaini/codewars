def solve(strings : list[str]) -> list[int]:
    return [sum([1 if x+1==ord(i[x].lower())-96 else 0 for x in range(len(i))]) for i in strings]

print(solve(["abb","ccc","vdsfefg"]))