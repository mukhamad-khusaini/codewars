def flick_switch(lst):
    state=True
    arr=[]
    for i in lst:
        if i.lower()!="flick":
            arr.append(state)
        else:
            state=not state
            arr.append(state)
        
    return arr