def find_it(seq):
    l=[seq.count(i)%2 for i in seq]
    s=[l.index(i) for i in l if i!=0]
    return seq[s[0]]


print(find_it([1,1,2,2,3,3,4,6,7,7,5,5,4,4,4]))

# Alternative
# def find_it(seq):
#     return [x for x in seq if seq.count(x) % 2][0]