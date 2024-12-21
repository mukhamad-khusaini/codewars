FIRST_NAME={}
SURNAME={}

def alias_gen(f_name, l_name):
    p=[]
    if(f_name[0].upper() in FIRST_NAME): p.append(FIRST_NAME[f_name[0].upper()])
    if(l_name[0].upper() in SURNAME): p.append(SURNAME[l_name[0].upper()])
    if(f_name[0].upper() not in FIRST_NAME or l_name[0].upper() not in SURNAME): return "Your name must start with a letter from A - Z."
    return " ".join(p)