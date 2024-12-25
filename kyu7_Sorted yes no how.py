def is_sorted_and_how(arr):
    asc_sort=sorted(arr)
    des_sort=sorted(arr,reverse=True)
    if arr==asc_sort: return 'yes, ascending'
    elif arr==des_sort: return 'yes, descending'
    else: return "no" 