def odd_or_even(arr):
    return "even" if abs(sum(arr))%2==0 else "odd"

print(odd_or_even([1,-2,-3]))