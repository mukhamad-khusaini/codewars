def to_jaden_case(string):
    str=[i for i in string.split(" ")]
    out=[]
    for i in str:
        temp=[]
        for x in range(len(i)):
            if x==0: temp.append(i[x].upper())
            else: temp.append(i[x].lower())
        
        out.append("".join(temp))
                

    return " ".join(out)

print(to_jaden_case("Hai hallo"))