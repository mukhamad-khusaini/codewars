def count_sheep(n):
    return "".join([f"{i+1} sheep..." for i in range(n)])

print(count_sheep(5))