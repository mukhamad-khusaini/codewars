def elevator_distance(array):
    return sum([abs(i-x) for i,x in zip(array, array[1:])])
