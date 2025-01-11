class Hero(object):
    name = ''
    position = 0
    health = ''
    damage = 0
    experience = 0
    def __init__(self, name='Hero'):
        #Add default values here
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
