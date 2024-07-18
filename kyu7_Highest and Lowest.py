def high_and_low(numbers):
    ls=[int(i) for i in numbers.split(" ")]
    return f'{max(ls)} {min(ls)}'


print(high_and_low("1 2 4 6 -1"))