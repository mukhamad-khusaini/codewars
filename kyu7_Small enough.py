def small_enough(array, limit):
    return not(False in [i<=limit for i in array])


print(small_enough([1,2,3,4,5], 2))