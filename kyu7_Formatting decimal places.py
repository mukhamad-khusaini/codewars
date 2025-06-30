def two_decimal_places(number):
    return float(str(number).split(".")[0]+"."+str(number).split(".")[1][:2])

print(two_decimal_places(34.77753))
# print("34.6754".split(".")[1][:2])