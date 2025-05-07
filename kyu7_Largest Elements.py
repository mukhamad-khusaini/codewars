def largest(n, xs):
    return sorted(sorted(xs,reverse=True)[:n:])

print(largest(3, [1,4,2,5,1,7,4,8]))