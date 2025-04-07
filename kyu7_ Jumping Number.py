def jumping_number(number):
    arr=[int(i) for i in str(number)]
    if len(arr)==1: return "Jumping!!"
    chk=[]
    for i in range(len(arr)):
        if i==0:
            chk.append(arr[i])
            continue
        if abs(chk[i-1]-arr[i])!=1:
            return "Not!!"
        if i==len(arr)-1 and abs(chk[i-1]-arr[i])==1:
            return "Jumping!!"
        else:
            chk.append(arr[i])

print(jumping_number(1234543219))