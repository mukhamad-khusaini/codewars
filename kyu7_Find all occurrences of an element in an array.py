def find_all(array, n):
    occ=[]
    arr=array
    for i in range(len(arr)):
        try:
            occ.append(arr.index(n))
            arr=arr[arr.index(n)+1:]
            print(arr)
        except:
            return occ

print(find_all([1,2,3,4,5,3,5],3))