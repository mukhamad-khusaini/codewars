def disemvowel(string_):
    return "".join(["" if i.lower() in ['a','i','u','e','o'] else i for i in string_])

print(disemvowel("Hai aku adalah kamu"))