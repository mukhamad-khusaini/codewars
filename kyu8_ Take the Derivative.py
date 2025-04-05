def derive(coefficient, exponent): 
    return f"{coefficient*exponent}x{'^' + str(exponent-1) if exponent>2 else ''}"

print(derive(2,2))