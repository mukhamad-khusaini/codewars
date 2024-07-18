def get_grade(s1, s2, s3):
    # Code here
    n=sum([s1,s2,s3])/3
    if(90<=n<=100):
        return 'A'
    elif(80<=n<90):
        return 'B'
    elif (70<=n<80):
        return 'C'
    elif (60<=n<70):
        return 'D'
    else:
        return 'F'