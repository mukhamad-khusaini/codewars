import math
def power_of_two(x):
  try:
    return str((math.log(x,2))).split(".")
  except:
    return False

print(power_of_two(590295810358705651719))