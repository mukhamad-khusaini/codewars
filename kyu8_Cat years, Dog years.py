def human_years_cat_years_dog_years(human_years):
    cat=0
    c=human_years
    while c!=0:
        if c != 1 and c != 2: cat+=4
        elif c==2: cat+=9
        else: cat+=15

        c-=1
    
    dog=0
    c=human_years
    while c!=0:
        if c != 1 and c != 2: dog+=5
        elif c==2: dog+=9
        else: dog+=15

        c-=1

    return [human_years,cat,dog]


print(human_years_cat_years_dog_years(10))