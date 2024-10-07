def find_digit(num, nth):
    return int(str(num)[::-1][nth-1]) if nth<=len(str(num)) and nth > 0 else 0 if nth > len(str(num)) else -1

print(find_digit(123,4))