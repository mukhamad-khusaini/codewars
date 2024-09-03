def whatday(num):
  return ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1] if num < 8 and num >= 1 else "Wrong, please enter a number between 1 and 7"