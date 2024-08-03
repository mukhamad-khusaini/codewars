def stairs_in_20(stairs):
    return sum([i*20 for i in [sum(x) for x in stairs]])