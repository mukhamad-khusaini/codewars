def move_ten(st):
    return "".join([chr(((ord(i)-86)%26 or 26)+96) for i in st])
print(move_ten('exampletesthere'))
# print(((ord('p')-86)%26))