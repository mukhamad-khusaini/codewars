def capitals(word):
    return [i for i in range(len(word)) if ord(word[i])>=65 and ord(word[i])<=90]

print(capitals("WosCS"))