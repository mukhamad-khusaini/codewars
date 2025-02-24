# input is an unsorted list of 3 positive integers
def pythagorean_triple(integers):
    i=sorted(integers)
    return i[0]**2 + i[1]**2 == i[2]**2