def score(dice):
    count=[]
    total=0
    for i in range(len(dice)+1): count.append(dice.count(i+1))
    for i in range(len(count)):
        if(i==0 and count[0]<3):
            for x in range(count[i]): total+=100
        elif(i==4 and count[4]<3):
            for x in range(count[i]): total+=50
        elif(i==0 and count[0]>=3):
            total+=1000
            if(count[0]%3>0):
                for x in range(count[0]%3): total+=100
        elif(i==4 and count[4]>=3):
            total+=500
            if(count[4]%3>0):
                for x in range(count[4]%3): total+=100
        elif(i==1 and count[1]>=3):
            total+=200
        elif(i==2 and count[2]>=3):
            total+=300
        elif(i==3 and count[3]>=3):
            total+=400
        elif(i==5 and count[5]>=3):
            total+=600
        
        

    return total


print(score([5,5,2,3,4]))