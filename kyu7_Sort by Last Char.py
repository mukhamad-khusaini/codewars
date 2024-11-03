def last(s):
    return sorted([i for i in s.split(" ")], key=lambda x: x[-1])