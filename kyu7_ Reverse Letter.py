def reverse_letter(st):
    strO=[i if i.isalpha() else "" for i in st]
    return "".join(strO[::-1])

print(reverse_letter("alp232?235624ha"))