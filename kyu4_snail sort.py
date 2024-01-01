def snail(snail_map):
    leng=len(snail_map)
    cont=snail_map
    out=[]
    c=0
    while c<1:
        for i in cont[0]:
            out.append(i)

        cont.pop(0)

        for i in range(len(cont[cont-1])-1):
            out.append(cont[i][leng-1])
            cont[i].pop(leng-1)

        
        for i in range(len(cont[len(cont)-1])):
            out.append(cont[len(cont)-1][-i+1])
        
        cont.pop(len(cont)-1)

        
        

        print(out)
        

        # out.append([*cont[leng-1]])
        # cont.pop(leng-1)


        c+=1

    return out

snail([[1,2,3],[4,5,6],[7,8,9]])


