def gps(s, x):
    if len(x)<=1: return 0
    return max([(abs(x[i]-x[i+1])/s)*60**2 for i in range(len(x)) if i!=len(x)-1])
