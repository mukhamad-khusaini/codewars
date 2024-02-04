def unique_in_order(sequence):
    l=[]
    c=len(sequence)-1
    i=0
    while c<=i:
        if len(sequence)==0:
            return l
        elif len(sequence)==1:
            l.append(sequence[i])
            return
        elif i==c:
            pass
        elif sequence[i]==sequence[i+1]:
            co=i
            lo=0
            while lo==c:
                if sequence[lo]==sequence[i]:
                    lo+=1
                else:
                    pass


        



            
    return l


print(unique_in_order("AAABaBB"))