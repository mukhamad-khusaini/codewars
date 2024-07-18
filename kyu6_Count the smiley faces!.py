def count_smileys(arr):
    counter=0
    for i in arr:
        lis=list(i)
        if(len(lis)==3):
            if((lis[0] == ":" or lis[0] == ";") and (lis[1] == "-"or lis[1] == "~") and (lis[2] == ")"or lis[2] == "D")):
                counter+=1
        else:
            if((lis[0] == ":"or lis[0] == ";") and (lis[1] == ")"or lis[1] == "D")):
                    counter+=1


    return counter

print(count_smileys([';]', ':)', ';D', ':~D', ';-D']))