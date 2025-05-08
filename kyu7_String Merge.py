def string_merge(string1, string2, letter):
    return ("".join(string1.split(letter)[0]) + letter + f"{letter}".join(string2.split(letter)[1:]))

print(string_merge("anatomy", "colotarga", "t"))