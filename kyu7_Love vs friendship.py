def words_to_marks(s):
    return sum([ord(i)-96 for i in s])

print(words_to_marks(2))