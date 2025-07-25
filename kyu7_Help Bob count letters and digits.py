def count_letters_and_digits(s):
    return sum([1 if i.isalnum() else 0 for i in s])