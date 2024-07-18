def array_diff(a, b):
    cont=[]
    if(len(b)==0):
        return a
    for x in range(len(a)):
        for y in range(len(b)):
            if(y==len(b)-1):
                if(a[x]!=b[y]):
                    cont.append(a[x])
                break
            elif(a[x]!=b[y]):
                continue
            else:
                break


    

    return cont

print(array_diff([1,2,3,4,5,5,4],[5]))