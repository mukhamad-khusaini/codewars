def compare(s1, s2):
    str1=[ord(i.upper()) if i.isalpha() else 0 for i in s1]
    str2=[ord(i.upper()) if i.isalpha() else 0 for i in s2]
    if 0 in str1 or s1 == "": str1 = 0
    if 0 in str2 or s2=="": str2 = 0

    if str1==0 and str2==0:
        return True
    elif str1==0 and type(str2)==type([]):
        return False
    elif str2==0 and type(str1)==type([]):
        return False
    else:
        return sum(str1)==sum(str2)


print("zs1".isalpha())