def strong_num(number):
    lst = [i for i in str(number)]
    ll=[]
    for i in lst:
        t=1
        for  x in range(1,int(i)+1):
            t*=x
        ll.append(t)
        t=1
    return 'STRONG!!!!' if sum(ll)==number else 'Not Strong !!'

print(strong_num(145))