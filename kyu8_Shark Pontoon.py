def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin: return "Alive!" if pontoon_distance/you_speed < shark_distance/(shark_speed/2) else "Shark Bait!"
    else: return "Alive!" if pontoon_distance/you_speed < shark_distance/shark_speed else "Shark Bait!"