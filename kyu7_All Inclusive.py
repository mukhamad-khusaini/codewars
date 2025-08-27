def contain_all_rots(strng, arr):
    rot=[]
    for i in range(len(strng)-1):
        rot.append(strng[i+1:]+strng[:i+1])
    
    rot.append(strng)

    return set(rot).issubset(arr)

print(contain_all_rots("bsjq",["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]))
# print("abcd"[:2])