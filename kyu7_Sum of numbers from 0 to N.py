def show_sequence(n):
    if n > 0: return f"{'+'.join([str(i) for i in range(n+1)])} = {sum([i for i in range(n+1)])}"
    elif n < 0: return f"{n}<0"
    elif n == 0: return "0=0"
    
print(show_sequence(-78))