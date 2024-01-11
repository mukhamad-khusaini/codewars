def xo(s):
    so=list(s.lower())
    return True if(so.count('o')==so.count('x')) else False

print(xo("OoOXx"))

# -- Alternative -- #
# def xo(s):
#     return s.lower().count('x') == s.lower().count('o')