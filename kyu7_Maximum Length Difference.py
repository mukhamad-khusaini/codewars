def mxdiflg(a1, a2):
    # your code
    return -1 if not a1 or not a2 else max(max([len(i) for i in a1])-min([len(i) for i in a2]),max([len(i) for i in a2])-min([len(i) for i in a1]))