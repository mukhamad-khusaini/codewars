def duplicate_count(text):
    arrText=list(text)
    counter=0
    dicts={}
    for i in range(len(arrText)):
        ind=arrText[i].lower()+""
        if(ind in dicts):
            dicts[ind].append(ind)
        else:
            dicts.update({ind:[ind]})
    
    for x in dicts:
        if(len(dicts[x])>1):
            counter+=1
    
    return counter
    
            
duplicate_count("AbdiNeGaraGasWasS")