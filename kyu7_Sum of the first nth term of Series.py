def series_sum(n):
    answer=0
    thr=1
    for i in range(n):
        answer+=1/thr
        thr+=3

    return "%.2f"%answer

print(series_sum(5))
    