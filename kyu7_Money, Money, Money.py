def calculate_years(principal, interest, tax, desired):
    if principal==desired: return 0
    cum=0
    y=0
    while cum < desired:
        if cum==0:
            cum+=principal+(principal*interest - ((principal*interest)*tax))
            y+=1
        else:
            cum+=(cum*interest - ((cum*interest)*tax))
            y+=1

    return y

print(calculate_years(1000,0.05,0.18,1000))