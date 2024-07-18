def duplicate_encode(word):
    d={}
    for i in word.lower(): 
        if i in d: d[f'{i}'].append(i)
        else: d.update({i: [i]})

    return ''.join(['(' if ((i in d) and (len(d[i])==1)) else ')' for i in word.lower()])

print(duplicate_encode("zxWBKuv"))


# Alternative
# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


# Note:
# 1. Use built-in 'count' function instead of using dictionary items maping