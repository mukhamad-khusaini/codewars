def distinct(seq):
    new=[]
    for i in seq:
        if i not in new: new.append(i)
    
    return new