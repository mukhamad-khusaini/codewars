def fly_by(lamps, drone):
    return ["o" if i < len(drone) else "x" for i in range(len(lamps))]

print(fly_by("xxxxx", "==T"))