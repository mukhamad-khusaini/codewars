def catch_sign_change(lst):
    global sign
    sign=""
    change=0

    for i in range(len(lst)):
        if i == 0:
            if lst[i]>=0:
                sign="p"
            else:
                sign="n"
        elif lst[i] >= 0:
            if sign == "p": continue
            else: 
                change+=1
                sign="p"
        elif lst[i] < 0:
            if sign == "n": continue
            else: 
                change+=1
                sign="n"
        
    return change
