def crap(garden, bags, cap):
    if sum([i.count("D") for i in garden]) > 0: return "Dog!!"
    return "Clean" if bags*cap-sum([i.count("@") for i in garden]) >=0 else "Cr@p"

print(crap([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']],2,2))