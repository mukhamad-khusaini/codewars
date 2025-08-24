def is_valid(formula):
    if {1,2}.issubset(formula) or {3,4}.issubset(formula): return False
    if (5 in formula and 6 not in formula) or (5 not in formula and 6 in formula): return False
    if 7 not in formula and 8 not in formula: return False
    return True

print(is_valid([5,6,7,8]))