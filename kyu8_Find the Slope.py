import math
def find_slope(points):
    return str(math.ceil((points[3]-points[1])/(points[2]-points[0]))) if abs(points[2]-points[0]) != 0 else "undefined"