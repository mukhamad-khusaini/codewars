def multi_table(number):
    return "".join([f"{i+1} * {number} = {(i+1)*number}\n" if i < 9 else f"{i+1} * {number} = {(i+1)*number}" for i in range(10)])

print(multi_table(4))
