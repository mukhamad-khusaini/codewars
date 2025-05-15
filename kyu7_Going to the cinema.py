import math
def movie(card, ticket, perc):
    def sysA(price, time):
        return price*time
    
    def sysB(cardPrice,price,time,percent):
        total=0
        priceOverTime=0
        i=0
        while i<time:
            if priceOverTime==0: 
                priceOverTime=price*percent
                total+=priceOverTime
                i+=1
            else:
                priceOverTime=priceOverTime*percent
                total+=priceOverTime
                i+=1
        
        return total+cardPrice

    syA=0
    syB=0
    i=1
    while math.ceil(syB)>=syA:
        syA+=sysA(ticket,i)
        syB+=sysB(card,ticket,i,perc)
        i+=1
    
    return i



print(movie(500, 15, 0.9))