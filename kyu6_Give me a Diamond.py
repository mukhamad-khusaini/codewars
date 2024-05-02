def diamond(n):
    if n%2==0 or n<1: return None                           # Default return if even or negative
    elif n==1: return "*\n"                                 # Default return if n = 1
    
    spaceCount=(n-1)/2                                      # Count how much space on the first "*"
    stringOut=[]                                            # For the result (Need to convert into string)
    astericCount=1                                          # Count how much asteric to be printed
    reverse=False                                           # Reverse condition (half end part of the diamond)
    laster=False                                            # Add middle part of the diamond (If this not exist, the middle part will not be added)
    
    for i in range(n):                                      # <MAIN PART>
        if astericCount==n and laster: reverse=True
        if reverse:
            spaceCount+=1
            for i in range(int(spaceCount)):
                stringOut.append(" ")
            
            astericCount-=2
            for i in range(astericCount):
                stringOut.append("*")
                

            stringOut.append("\n")
        
        else:
            for i in range(int(spaceCount)):
                stringOut.append(" ")
            
            if astericCount!=n: spaceCount-=1
            
            for i in range(astericCount):
                stringOut.append("*")
            
            if astericCount==n: laster=True
            if astericCount!=n: astericCount+=2

            stringOut.append("\n")

    return "".join(stringOut)                               # <OUTPUT THE RESULT>

print(diamond(3))