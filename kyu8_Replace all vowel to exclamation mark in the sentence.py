def replace_exclamation(st):
    return "".join(["!" if i.lower() in ["a","i","u","e","o"] else i for i in st])