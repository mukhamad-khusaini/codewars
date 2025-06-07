import math
def find_slope(points):
    return "undefined" if points[2]-points[0]==0 else str(math.trunc((points[3]-points[1])/(points[2]-points[0])))