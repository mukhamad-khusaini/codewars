def tower_builder(n_floors):
    current=1
    pyr=[]
    for i in range(n_floors):
        sp=n_floors-(i+1)
        s=list("*"*current)
        s.insert(0, " "*sp)
        s.insert(len(s), " "*sp)
        pyr.append(''.join(s))
        current+=2

    return pyr

print(tower_builder(3))