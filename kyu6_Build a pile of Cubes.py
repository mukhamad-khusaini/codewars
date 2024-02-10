# !!! WARNING : SMALL NUMBER ONLY
def find_nb(m):
    if(m<0): return -1
    n=0
    while True:
        t=0
        for i in range(n):
            t+=((n-i)**3)
            
        if(t==m):
                return n
        elif(t>m):
                return -1
        else:
            n+=1

    

print(find_nb(26825883955641))

# Alternative (This more faster)
# def find_nb(m):
#     n = 1
#     while True:
#         m -= n**3
#         if m == 0:
#             return n
#         elif m < 0:
#             return -1
#         else:
#             n += 1