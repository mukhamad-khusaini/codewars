def no_boring_zeros(n):
    if not n: return n
    num=list(str(n))
    i=True
    while i:
        if num[-1] == "0": del num[-1]
        else: return int("".join(num))

print(no_boring_zeros(230))