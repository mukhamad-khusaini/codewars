def alternate_case(s):
    return " ".join(["".join([x.swapcase() for x in i]) for i in s.split(" ")])

print(alternate_case("Hello World!"))