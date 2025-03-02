def max_diff(lst):
    if not lst: return 0
    return sorted(lst)[-1] - sorted(lst)[0]