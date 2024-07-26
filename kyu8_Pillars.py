def pillars(num_pill, dist, width):
    if num_pill==1: return 0
    elif num_pill==2: return dist*100
    else: return ((num_pill-2)*width)+((num_pill-1)*dist*100)
    
    
print(pillars(11, 15, 30))