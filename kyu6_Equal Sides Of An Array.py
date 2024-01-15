def find_even_index(arr):
    for i in range(len(arr)):
        if(sum(arr[:i])==sum(arr[(i+1):])): return i
    
    return -1
        
        
        

print(find_even_index([10,-80,10,10,15,35,20]))