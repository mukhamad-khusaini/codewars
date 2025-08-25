def arithmetic_sequence_elements(a, d, n):
    rn=[]
    for i in range(n):
        if not rn:
            rn.append(a)
        else:
            rn.append(rn[i-1]+d)
    
    return ", ".join([str(i) for i in rn])

print(arithmetic_sequence_elements(1,2,5))