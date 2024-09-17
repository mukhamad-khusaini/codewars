def even_numbers(arr,n):
    return [i for i in arr if i%2==0][-n:]

print(even_numbers([1,2,3,4,5,6,7,8,9,10],4))