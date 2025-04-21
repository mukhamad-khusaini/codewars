import math
def predict_age(*args):
    return math.floor(math.sqrt(sum(i*i for i in args))/2)