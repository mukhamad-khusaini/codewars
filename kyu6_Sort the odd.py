def sort_array(source_array):
    lo,lio=[i for i in source_array if i%2!=0],['*' if i%2!=0 else i for i in source_array]
    lo.sort()
    return [lo.pop(0) if i=='*' else i for i in lio]

print(sort_array([2,4,1,5,4,9,4,6,7,3,2,1]))

# Alternative
# def sort_array(source_array):
#     odds = iter(sorted(v for v in source_array if v % 2))
#     return [next(odds) if i % 2 else i for i in source_array]