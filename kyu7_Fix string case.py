def solve(s):
    c=[0 if i.islower() else 1 for i in s]
    lower=c.count(0)
    upper=c.count(1)
    return s.upper() if lower<upper else s.lower()