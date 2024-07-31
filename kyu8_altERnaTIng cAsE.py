def to_alternating_case(string):
    return "".join([i.lower() if i==i.upper() else i.upper() for i in string])


print(to_alternating_case("Ab6S3k1A"))
