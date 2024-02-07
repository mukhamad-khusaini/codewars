def unique_in_order(sequence):
    l=[]
    c=len(sequence)
    i=0
    while i<c:
        if len(sequence)==0:
            return l
        elif len(sequence)==1:
            l.append(sequence[i])
            return l
        elif i==len(sequence)-1:
            l.append(sequence[i])
            break
        elif sequence[i]==sequence[i+1]:
            lo=0
            if(i+lo==c): 
                l.append(sequence[i])
                break
            while i+lo<c:
                if sequence[i]==sequence[i+lo]:
                    lo+=1
                else:
                    break

            l.append(sequence[i])
            i+=lo

            
        else:
            l.append(sequence[i])
            i+=1
            
    return l


print(unique_in_order("PPPPVVVtBVVUUUPPPxxxxxQQQnnnddT"))


# Alternative
# def unique_in_order(iterable):
#     result = []
#     prev = None
#     for char in iterable[0:]:
#         if char != prev:
#             result.append(char)
#             prev = char
#     return result