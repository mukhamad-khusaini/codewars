def get_ages(sum_, difference):
    if sum_ < 0 or difference < 0 or sum_/2-difference/2 < 0: return None
    return (sum_/2+difference/2, sum_/2-difference/2)