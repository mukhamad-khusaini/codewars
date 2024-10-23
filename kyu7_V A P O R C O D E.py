def vaporcode(s):
    return "  ".join(list("".join([i for i in s.split(" ")]).upper()))

print(vaporcode("syam bia"))