def is_isogram(string):
    return sum([string.lower().count(i) for i in string.lower()])==len(string)

print(is_isogram("ada"))