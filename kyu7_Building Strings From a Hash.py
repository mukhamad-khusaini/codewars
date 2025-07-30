def solution(pairs):
    return ",".join([ f"{i} = {x}" for i,x in zip(pairs.keys(), pairs.values())])
print(solution({'a':1, 'b':2}))