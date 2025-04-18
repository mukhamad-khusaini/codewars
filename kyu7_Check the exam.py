def check_exam(arr1,arr2):
    point=0
    for i in range(len(arr1)):
        if arr1[i]==arr2[i]: point+=4
        elif arr1[i]!=arr2[i] and arr2[i]: point-=1
        else: point+=0
    
    return point if point>0 else 0


print(check_exam(['a','b','c'],['b','c','d']))