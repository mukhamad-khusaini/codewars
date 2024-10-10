def split_and_merge(string_, separator):
    return " ".join([f"{separator}".join(list(x)) for x in [i for i in string_.split(" ")]])

print(split_and_merge("My name is John", "-"))