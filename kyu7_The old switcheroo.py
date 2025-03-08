def vowel_2_index(string):
    return "".join([string[i] if string[i].lower() not in ['a','i','u','e','o'] else str(i+1) for i in range(len(string))])