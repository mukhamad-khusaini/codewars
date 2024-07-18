def remove_char(s):
    c=list(s)
    c.pop(0)
    c.pop(-1)
    return "".join(c)

print(remove_char("Hallo"))