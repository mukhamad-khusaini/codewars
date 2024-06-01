def is_uppercase(arr):
    return False if True in [True if ord(i) in list(range(97,123)) else False for i in arr] else True