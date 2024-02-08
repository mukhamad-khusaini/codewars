def rot13(message):
    return "".join([ (chr((ord(i)+13)-26) if(90<(ord(i)+13)<104 or (ord(i)+13)>122) else chr(ord(i)+13)) if(65<=ord(i)<=90 or 97<=ord(i)<=122) else i for i in message])

print(rot13('Test'))

# Alternative
# def rot13(message):
#     return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))