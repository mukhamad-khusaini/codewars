import math
def to_time(seconds):
    hour=(seconds/60)/60
    minute=math.floor((hour-math.floor(hour))*60)
    return f'{math.floor(hour)} hour(s) and {minute} minute(s)'