import math
def movie(card, ticket, perc):
    sysA=0
    sysB=0
    i=1
    while math.ceil(sysB)>=sysA:
        sysA=ticket*i
        sysB=sum([ticket*(perc**c) for c in range(1,i+1)])
        sysB+=card
        if math.ceil(sysB)<sysA: return i
        i+=1

    return i


print(movie(500, 15, 0.9))