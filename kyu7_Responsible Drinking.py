import re
def hydrate(drink_string): 
    coun=sum([int(i) for i in re.findall(r'\d+', drink_string)])
    return "1 glass of water" if coun == 1 else f"{coun} glasses of water"

print(hydrate("1 gass 3 asda 35 asdads"))