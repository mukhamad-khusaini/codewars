def product_fib(_prod):
    fib=[0,1,1]
    while True:
        if(fib[0]*fib[0+1]==_prod):
            return [0,1, True]
        elif(fib[0]*fib[0+1]>=_prod):
            return [0,1, False]
        elif(fib[1]*fib[2]==_prod):
            return [1,1, True]
        elif(fib[1]*fib[2]>=_prod):
            return [1,1, False]
        else:
            fib.append(fib[-1]+fib[-2])
            if(fib[-1]*fib[-2]==_prod):
                return [fib[-2], fib[-1], True]
            elif(fib[-1]*fib[-2]>=_prod):
                return [fib[-2], fib[-1], False]
            continue
        


print(product_fib(1))

# Alternative (a b interchange)
# def productFib(prod):
#   a, b = 0, 1
#   while prod > a * b:
#     a, b = b, a + b
#   return [a, b, prod == a * b]