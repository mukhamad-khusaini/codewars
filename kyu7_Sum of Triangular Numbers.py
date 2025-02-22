def sum_triangular_numbers(n):
    #your code here
    num=0
    summ=[]
    for i in range(1,n+1):
        num=num+i
        summ.append(num)
    return sum(summ)

sum_triangular_numbers(6)