def number_to_pwr(number, p): 
    if p==0: return 1
    temp=number
    for i in range(p-1):
        temp=temp*number
        
    return temp

print(number_to_pwr(3,2))