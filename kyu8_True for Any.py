def any_(lst, func): 
    if not lst: return False
    return True if True in [func(i) for i in lst] else False