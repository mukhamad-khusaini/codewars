def filter_long_words(sentence, n):
    return [i for i in sentence.split(" ") if len(i)>n]