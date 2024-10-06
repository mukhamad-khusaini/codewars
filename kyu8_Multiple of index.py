def multiple_of_index(arr):
    return [arr[i] for i in range(len(arr)) if (i!=0 and arr[i]%i==0) or arr[i]==0]

print(multiple_of_index([22, -6, 32, 82, 9, 25]))