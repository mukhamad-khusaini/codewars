def max_tri_sum(numbers):
    return sum(sorted((set(numbers)))[::-1][:3])

print(max_tri_sum([3,2,6,8,2,3,9,99,88]))