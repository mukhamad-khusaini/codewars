def fillable(stock, merch, n):
    return stock[merch] - n >=0 if merch in stock else False