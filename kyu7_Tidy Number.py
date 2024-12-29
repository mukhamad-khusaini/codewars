def tidyNumber(n):
    num=list(str(n))
    for i in range(len(num)-1):
      
        if num[i]>num[i+1]: return False
      
    return True


print(tidyNumber(12345))