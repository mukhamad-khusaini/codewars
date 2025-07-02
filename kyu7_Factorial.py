import math
def factorial(n):
    if n<0 or n>12:
        raise ValueError()
    return math.factorial(n)

print(factorial(7))