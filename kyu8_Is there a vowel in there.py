def is_vow(inp):
    return [ord(i) if type(i)==type("sa") else i for i in inp ]

print(is_vow(123))