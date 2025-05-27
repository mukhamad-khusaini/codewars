import math

def square_area(arc_length):
    # Compute the radius using the arc length formula for a quarter-circle
    radius = (2 * arc_length) / math.pi
    # Compute the area of the square
    area = radius ** 2
    # Return the result rounded to two decimals
    return round(area, 2)