
def fuel_price(litres, price_per_litre):
    price_per=price_per_litre*100
    price=litres*price_per
    discount=(litres-litres%2)*2.5
    if discount>25:
        discount=25
    return float(f"{(price-(litres*discount))/100:.2f}")