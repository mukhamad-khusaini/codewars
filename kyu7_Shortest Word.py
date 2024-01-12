def find_short(s):
    return min([len(i) for i in s.split(" ")])

print(find_short("I become so numb"))