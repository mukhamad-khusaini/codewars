def array(string):
    strArr=string.split(",")
    if len(strArr)<=2: return None
    return " ".join([strArr[i] for i in range(len(strArr)) if (i!=0 and i!=len(strArr)-1)])

print(array(""))