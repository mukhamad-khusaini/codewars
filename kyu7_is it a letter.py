def is_letter(s):
    # your code here
    return True if len(s)==1 and s.isalpha() else False

print(is_letter("X"))