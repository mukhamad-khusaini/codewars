def diamond(n):
    if n%2==0 or n<1: return None       # Default return if even or negative
    elif n==1: return "*\n"             # Default return if n = 1
    
    spaceCount=(n-1)/2                  # Count how much space on the first "*"
    stringOut=[]                        # For the result (Need to convert into string)
    for i in range(n):
                                        # YOU LEAVE YOUR JOB HERE!
        pass

print(diamond(1))