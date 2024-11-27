def find_smallest(numbers, to_return):
    if to_return=='value': return min(numbers)
    else : return numbers.index(min(numbers))