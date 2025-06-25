
def sum_of_n(n):
    def sumx(x):
        return sum([i for i in range(x+1)])

    ret=[]
    for i in range(abs(n)+1):
        if n>0:
            ret.append(sumx(i))
        elif i==0:
            ret.append(0)
        else:
            ret.append(sumx(i)*-1)
    return ret

