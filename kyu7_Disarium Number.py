def disarium_number(number):
    num=[int(i) for i in str(number)]
    ext=[num[i]**(i+1) for i in range(len(num))]
    return "Disarium !!" if sum(ext)==number else "Not !!"