def sum_two_smallest_numbers(numbers):
    low=min(numbers)
    numbers.remove(min(numbers))
    low2=min(numbers)
    return low+low2

print(sum_two_smallest_numbers([1,2,3,4,5]))