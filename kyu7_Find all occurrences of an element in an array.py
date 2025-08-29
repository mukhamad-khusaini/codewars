def find_all(array, n):
    return [i for i in range(len(array)) if array[i]==n]

print(find_all([1,2,3,4,5,3,5],3))