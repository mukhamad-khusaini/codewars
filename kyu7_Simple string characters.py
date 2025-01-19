def solve(s):
    up=sum([1 for i in s if ord(i) in range(65,91)])
    low=sum([1 for i in s if ord(i) in range(97,123)])
    num=sum([1 for i in s if ord(i) in range(48,58)])
    spc=len(s)-up-low-num
    return [up,low,num,spc]