def vert_mirror(strng):
    st=strng.split("\n")
    return "\n".join([i[::-1] for i in st])
    
def hor_mirror(strng):
    st=strng.split("\n")
    return "\n".join(st[::-1])
    
def oper(fct, s):
    return fct(s)

print(oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"))