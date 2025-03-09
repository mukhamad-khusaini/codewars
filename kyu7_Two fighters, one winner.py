class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(fighter1: Fighter, fighter2: Fighter, first_attacker):
    if first_attacker==fighter1.name:
        health1=fighter1.health
        health2=fighter2.health
        turns=0
        while health1>0 and health2>0:
            if turns==0:
                health2=health2-fighter1.damage_per_attack
                turns=1
            else:
                health1=health1-fighter2.damage_per_attack
                turns=0
        return fighter1.name if health1>0 else fighter2.name
    else:
        health1=fighter1.health
        health2=fighter2.health
        turns=1
        while health1>0 and health2>0:
            if turns==0:
                health2=health2-fighter1.damage_per_attack
                turns=1
            else:
                health1=health1-fighter2.damage_per_attack
                turns=0
        return fighter1.name if health1>0 else fighter2.name