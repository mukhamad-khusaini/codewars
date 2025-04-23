def special_number(number):
    return "Special!!" if False not in [True if int(i) in [0,1,2,3,4,5] else False for i in list(str(number))] else "NOT!!"