def square_digits(num):
    arr=list(str(num))
    return int("".join([str(int(i)**2) for i in arr]))

print(square_digits(928))