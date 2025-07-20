def initialize_names(name):
    arrN=name.split(" ")
    if arrN[1:-1]:
        return arrN[0] + " " + " ".join([f"{i[0]}." for i in arrN[1:-1]]) + " " + arrN[-1]
    else: return name

print(initialize_names("Pter John Fucl Khannedy Jamet"))