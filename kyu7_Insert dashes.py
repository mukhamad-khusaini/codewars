def insert_dash(num):
    strNum=str(num)
    if len(strNum)==1: return strNum
    return "".join(([i + "-" if int(i)%2!=0 and int(x)%2!=0 else i for i,x in zip(strNum,strNum[-(len(strNum)-1):]+"2")]))

print(insert_dash(454793))