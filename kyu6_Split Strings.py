def solution(s):
    arr=list(s)
    arrCont=[]
    inc=0
    while inc<len(arr):
        if(inc<len(arr)-1):
            if(inc+2<=len(arr)):
                arrCont.append("%s%s"%(arr[inc],arr[inc+1]))
                inc+=2
            else:
                arrCont.append(arr[inc]+"_")
                break
        else:
            arrCont.append(arr[inc]+"_")
            break
    
    print(arrCont)


solution("andisaasdfass")