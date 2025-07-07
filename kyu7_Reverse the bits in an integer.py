def reverse_bits(n):
    bit=bin(n)
    return int(bit[2:][::-1],2)

print(reverse_bits(12))