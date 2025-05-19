import math
def dating_range(age):
    if age<=14:
        return f"{math.floor(age-0.10*age)}-{math.floor(age+0.10*age)}"
    else:
        return f"{math.floor(age/2+7)}-{math.floor(2*(age-7))}"