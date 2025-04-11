def arithmetic(a, b, operator):
    switcher={
        'add': lambda: a+b,
        'subtract': lambda: a-b,
        'multiply': lambda: a*b,
        'divide': lambda: a/b,
    }

    return switcher[operator]()

print(arithmetic(5,2,"add"))