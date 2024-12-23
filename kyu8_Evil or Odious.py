def evil(n):
    return "It's Evil!" if str(format(n,'b')).count('1')%2==0 else "It's Odious!"

print(evil(3))