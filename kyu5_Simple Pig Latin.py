def pig_it(text):
    stri=text.split(" ")
    container=[]
    for i in stri:
        if(i != "!" and i != "?"):
            tempStr=list(i)
            cont=tempStr.pop(0)
            tempStr.append(cont + "ay")
            strJoin="".join(tempStr)
            container.append(strJoin)
        else:
            container.append(i)
    
    return " ".join(container)

print(pig_it("Hello world ?"))