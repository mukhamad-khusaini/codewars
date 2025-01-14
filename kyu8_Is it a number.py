def is_digit(s):
    try:
        float(s)
        return True
    except:
        return False
    

# ss=float("-0")
# print(ss)

print(is_digit("-2.22"))