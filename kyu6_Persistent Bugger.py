def persistence(n):
    c=0
    def rep(n):
        nonlocal c
        nt=1
        if (len(str(n))!=1):
            t=list(str(n))
            for i in range(len(t)):
                nt=nt*int(t[i])
            c+=1
            rep(nt)
    rep(n)
    return c



print(persistence(123))
# print(len(str(39)))