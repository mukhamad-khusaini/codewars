def printer_error(s):
    return f"{len([i for i in s if ord(i)>109])}/{len(s)}"

print(printer_error("abcknop"))