def difference_of_squares(n):
    return abs(sum([i for i in range(1,n+1)])**2 - sum([i**2 for i in range(1,n+1)]))


# print(difference_of_squares(10))