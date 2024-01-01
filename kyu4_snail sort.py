def snail(snail_map):
    if(snail_map==[[]]): return []
    cont=snail_map
    out=[]
    while True:
        if(len(cont)==0): return out
        elif(len(cont[0])==1): 
            out.append(cont[0][0])
            return out
        
        for i in cont[0]:
            out.append(i)

        cont.pop(0)

        for i in range(len(cont)):
            out.append(cont[i][len(cont[i])-1])
            cont[i].pop(len(cont[i])-1)

        for i in range(len(cont)):                
            out.append(cont[-1][-1])
            cont[-1].pop(-1)   
        
        cont.pop(len(cont)-1)
       

        for i in range(len(cont)):
            out.append(cont[-1-i][0])
            cont[-1-i].pop(0)
        
print(snail([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))