def seven_ate9(str_):
    while "797" in str_:
        str_ = str_.replace("797", "77")
    return str_
    
print(seven_ate9("124579797"))