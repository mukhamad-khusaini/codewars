def hello(name=""):
    if name=="": return "Hello, World!"
    else: return f"Hello, {name[0].upper()}{name[1:].lower()}!"


print(hello("jiKa"))