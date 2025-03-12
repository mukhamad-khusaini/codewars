def sum_of_integers_in_string(s):
    num=[]
    temp=[]
    for i in range(len(s)):
        if s[i].isnumeric():
            if i==len(s)-1:
                temp.append(s[i])
                num.append(''.join(temp))
            else:
                temp.append(s[i])
        else:
            num.append(''.join(temp))
            temp=[]

    return sum([int(i) for i in num if i.isnumeric()])

print(sum_of_integers_in_string("alg3br4inj10l9000"))