import math

def find_next_square(sq):
    if math.sqrt(sq)-int(math.sqrt(sq))==0: return (math.sqrt(sq) + 1)**2
    return -1
