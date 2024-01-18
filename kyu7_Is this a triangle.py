def is_triangle(a, b, c):
    return (a+b>c) and (b+c>a) and (a+c>b)

print(is_triangle(-1,-1,-1))
