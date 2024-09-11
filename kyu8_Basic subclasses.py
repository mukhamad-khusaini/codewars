class Human():
    def __init__(self):
        self.base_property = "I am the base property"

class Man(Human):
     def __init__(self):
        self.base_property = "I am the base property"
class Woman(Human):
     def __init__(self):
        self.base_property = "I am the base property"



def God():
    return [Man(),Woman()]