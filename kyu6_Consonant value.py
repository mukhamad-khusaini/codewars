def solve(s):
    splitter="".join([i if i not in ["a","i","u","e","o"] else " " for i in s]).split(" ")
    return max([sum([ord(x)-96 for x in i]) for i in splitter])

print(solve("strength"))