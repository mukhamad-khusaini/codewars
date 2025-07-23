def vowel_one(s):
    ref=["a","i","u","e","o"]
    return "".join(["1" if i in ref else "0" for i in s.lower()])