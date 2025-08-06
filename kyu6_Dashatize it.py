def dashatize(n):
    strr= "".join([f"-{i}-" if int(i)%2!=0 else i for i in str(abs(n))]).replace("--","-")
    if strr[len(strr)-1]=="-": strr=strr[:len(strr)-1]
    if strr[0]=="-": strr=strr[1:]
    return strr

print(dashatize(122457))