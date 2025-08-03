def next_happy_year(year):
    y=year+1
    while True:
        if len(set(str(y))) == len(str(year)):
            return y
        else: y=y+1

print(set(str(1229)))