def nickname_generator(name):
    if len(name)<4: return "Error: Name too short"
    if name[2] in ["a","i","u","e","o"]: return name[:4]
    else: return name[:3]

print(nickname_generator("Jaoon"))