def men_from_boys(arr):
    num=set(arr)
    even=sorted([i for i in num if i%2==0])
    odds=sorted([i for i in num if i%2!=0], reverse=True)
    return even+odds