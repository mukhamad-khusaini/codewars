def get_count(sentence):
    return sentence.count('a')+sentence.count('i')+sentence.count('u')+sentence.count('e')+sentence.count('o')

print(get_count("aiueo"))

# Alternative
# def getCount(s):
    # return sum(c in 'aeiou' for c in s)