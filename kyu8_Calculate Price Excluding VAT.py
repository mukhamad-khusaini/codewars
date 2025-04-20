def excluding_vat_price(price):
    return -1 if not price else round((price/115)*100,2)