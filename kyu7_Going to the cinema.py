import math
def movie(card, ticket, perc):
    time=0
    t=0
    p=card
    vem=0
    while math.ceil(p)>t:
        if vem==0: vem=ticket*perc
        else: vem=vem*perc
        p+=vem
        t+=ticket
        time+=1
    
    return time

print(movie(500, 15, 0.9))