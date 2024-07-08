def mango(quantity, price):
    if quantity<3: return quantity*price
    t=0
    t+=quantity%3*price
    quantity-=quantity%3
    t+=(quantity/3)*2*price
    return int(t)
    
    
print(11//3)