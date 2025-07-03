def calculate(s):
    plus="+".join(s.split("plus"))
    minus="-".join(plus.split("minus"))

    return str(eval(minus))

print(calculate("1minus1plus3plus4minus5"))