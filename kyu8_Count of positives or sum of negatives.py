def count_positives_sum_negatives(arr):
    if arr==[]: return []
    return [len([i for i in arr if i>0]), sum([i for i in arr if i<0])]