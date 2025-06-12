import math
def product_array(numbers):
    return [math.prod(numbers)/numbers[i] for i in range(len(numbers))]
