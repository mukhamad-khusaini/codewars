import math
def round_it(n):
    sub=list(str(n).split("."))
    if len(sub[0]) < len(sub[1]): return math.ceil(n)
    elif len(sub[0]) > len(sub[1]): return math.floor(n)
    else: return round(n)