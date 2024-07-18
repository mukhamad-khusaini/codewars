def nb_year(p0, percent, aug, p):
    c=0
    while p0 < p:
        c+=1
        p0+=int((p0*(percent/100))+aug)
    
    return c

print(nb_year(1500, 5, 100, 5000))
# print(1500+(1500*(5/100))+100)

