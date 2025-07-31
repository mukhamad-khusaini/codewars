def is_lucky(n):
    sstr=str(n)
    return sum([int(i) for i in sstr])%9==0