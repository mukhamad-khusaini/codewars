def solve(arr): 
    seen = set()
    result = []
    for item in reversed(arr):
        if item not in seen:
            seen.add(item)
            result.append(item)
    return list(reversed(result))
print(solve([3,4,4,3,6,3]))