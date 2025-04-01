import unicodedata
def correct_polish_letters(st): 
    return unicodedata.category(unicodedata.normalize("NKFD",st))

print(correct_polish_letters("s"))