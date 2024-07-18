def solution(number):
    cont=[]
    res=0
    for i in range(number):
        if(i%3==0 or i%5==0):
            if(i==0):
                continue
            cont.append(i)
    
    for i in cont:
        res+=i

    return res

print(solution())