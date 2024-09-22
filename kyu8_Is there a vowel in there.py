def is_vow(inp):
    return [chr(i) if chr(i) in ["a","i","u","e","o"] else i for i in inp]

print(is_vow(123))