def sum_digits(number):
    return sum([abs(int(i)) for i in str(number) if i!="-"])