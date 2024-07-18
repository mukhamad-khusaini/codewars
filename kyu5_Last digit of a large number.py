def last_digit(a, b):
    if b == 0:
        return 1
    else:
        return pow(a, b, 10)

print(last_digit(4,1))