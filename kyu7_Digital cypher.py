def encode(message, key):
    keyArr=[int(i) for i in list(str(key))]

    return [ord(message[i])-96+keyArr[i%len(keyArr)] for i in range(len(message.lower()))]

print(encode('s',21))

# print(4%4)