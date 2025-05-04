def solve(a,b):
    frs="".join([i for i in a if i not in b])
    scn="".join([i for i in b if i not in a])
    return "".join([frs,scn])

print(solve("xbys","xjyl"))