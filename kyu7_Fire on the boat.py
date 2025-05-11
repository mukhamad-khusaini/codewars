def fire_fight(s):
    return " ".join(["~~" if i.lower()=="fire" else i for i in s.split(" ")])