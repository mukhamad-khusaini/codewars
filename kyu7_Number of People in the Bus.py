def number(bus_stops):
    return sum([i[0] for i in bus_stops])-sum([i[1] for i in bus_stops])

print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))