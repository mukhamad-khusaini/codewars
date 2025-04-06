def solve(s):
    if not s: return 0
    main=[]
    arrs=[]
    for i in range(len(s)):
        if s[i] in ['a','i','u','e','o']:
            if i==len(s)-1:
                arrs.append(s[i])
                main.append("".join(arrs))
            arrs.append(s[i])
        else:
            main.append("".join(arrs))
            arrs=[]
    
    return max(len(i) for i in main)

print(solve("ebolpgewielvildauiocieioie"))