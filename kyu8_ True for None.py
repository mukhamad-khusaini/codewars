def none(lst, func):
    return True if True not in [func(i) for i in lst] or not lst else False

