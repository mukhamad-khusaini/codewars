def fly_by(lamps, drone):
    return "".join(["o" if i < len(drone) else "x" for i in range(len(lamps))])

print(fly_by("xxxxx", "==T"))