def high(x):
    value=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    strList=x.split(" ")
    scoreContainer=[]
    for i in strList:
        scr=0
        for x in i:
            scr+=value.index(x)+1
        scoreContainer.append(scr)
    
    return strList[scoreContainer.index(max(scoreContainer))]

print(high("aas bx"))
        
