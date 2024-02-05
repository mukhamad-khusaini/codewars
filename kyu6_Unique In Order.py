def unique_in_order(sequence):
    l=[]
    c=len(sequence)-1
    i=0
    while i<=c:
        if len(sequence)==0:
            return l
        elif len(sequence)==1:
            l.append(sequence[i])
            return l
        elif i==c:
            l.append(sequence[i])
            break
        elif sequence[i]==sequence[i+1]:
            lo=0
            while i+lo<=c:
                if sequence[i]==sequence[i+lo]:
                    lo+=1
                else:
                    l.append(sequence[i])
                    i+=lo
                    break
            if(i+lo==c+1): 
                l.append(sequence[i])
                break
        else:
            l.append(sequence[i])
            i+=1
            
    return l


print(unique_in_order("PPPPVVVtBVVUUUPPPxxxxxQQQnnnddT"))