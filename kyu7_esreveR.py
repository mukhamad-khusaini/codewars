def reverse(lst):
    x = list()
    i=-1
    while i!=len(lst)-(len(lst)*2+1):
        x.append(lst[i])
        i-=1
    return x

print(reverse([0,"23",True,21,"ss"]))