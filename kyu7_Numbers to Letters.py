def switcher(arr):
    alp=sorted(list(map(chr,range(ord('a'),ord('z')+1))),reverse=True)+['!',"?"," "]
    ll={}
    for i in range(29):
        ll[f"{i+1}"]=alp[i]
    return "".join([ll[i] for i in arr])

print(switcher(['24', '12', '23', '22', '4', '26', '9', '8']))