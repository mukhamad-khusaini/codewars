def is_divisible(*args):
    return False if False in [args[0]%i==0 for i in args[1:]] else True

print([1,2,3,4,5][1:])