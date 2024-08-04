def define_suit(card):
    obj={
        "H": "hearts",
        "C": "clubs",
        "S": "spades",
        "D": "diamonds"
    }
    
    return obj[card[-1]]

print(define_suit("9C"))