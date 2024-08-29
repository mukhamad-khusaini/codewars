# write the function is_anagram
def is_anagram(test, original):
    ohm=list(original.lower())
    for i in test.lower():
        if i in ohm: ohm.pop(ohm.index(i))
        else: return False
    if len(ohm)>0: return False
    return True