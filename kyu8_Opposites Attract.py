def lovefunc( flower1, flower2 ):
    return (flower1%2==0 and flower2%2!=0) or (flower2%2==0 and flower1%2!=0)

print(lovefunc(0,1))