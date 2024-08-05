def remove_exclamation_marks(s):
    return "".join(list(filter(lambda a: True if (a!="!") else False, s)))

print(remove_exclamation_marks("He!llo! world!"))