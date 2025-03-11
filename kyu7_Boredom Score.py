def boredom(staff):
    acc=len([i for i in staff if staff[i] == 'accounts'])*1
    fi=len([i for i in staff if staff[i] == 'finance'])*2
    can=len([i for i in staff if staff[i] == 'canteen'])*10
    reg=len([i for i in staff if staff[i] == 'regulation'])*3
    trd=len([i for i in staff if staff[i] == 'trading'])*6
    chg=len([i for i in staff if staff[i] == 'change'])*6
    iss=len([i for i in staff if staff[i] == 'IS'])*8
    ret=len([i for i in staff if staff[i] == 'retail'])*5
    cln=len([i for i in staff if staff[i] == 'cleaning'])*4
    pa=len([i for i in staff if staff[i] == 'pissing about'])*25

    ssm=sum([acc,fi,can,reg,trd,chg,iss,ret,cln,pa])

    return 'kill me now' if ssm<=80 else 'i can handle this' if ssm>80 and ssm<100 else 'party time!!'