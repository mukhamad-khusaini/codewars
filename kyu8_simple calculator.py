def calculator(x,y,op):
    if op not in ["+","-","/","*"] or type(op)==type(2) or type(y) != type(2) or type(x) != type(2): return "unknown value"
    return eval(f"{x}{op}{y}")

print(calculator(218, 829, "o"))