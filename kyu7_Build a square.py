def generate_shape(n):
    tep=[]
    for i in range(n):
        for x in range(n):
            tep.append("+")
        tep.append("\n")
        
    tep.pop()
    return "".join(tep)

print(generate_shape(3))