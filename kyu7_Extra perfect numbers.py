def extra_perfect(n: int) -> list[int] :
    #your code here
    return [i for i in range(1,n+1) if str(bin(i)).split("0b")[1].startswith("1") and str(bin(i)).split("0b")[1].endswith("1")]

print(extra_perfect(7))