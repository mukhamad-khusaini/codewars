import math
def is_square(n):    
    return False if (n<0) else math.sqrt(n)-int(math.sqrt(n))==0

print(is_square(2))

# Alternative
# import math
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0