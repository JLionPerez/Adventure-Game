import profession

class Character:
    # default variables
    name = ""
    profession = ""
    health = 0
    spells = {
        "Light Heal" : ["heal", 5],
        "Burn" : ["attack", 2],
        "Frost" : ["attack", 3]
    }

    # constructor
    def __init__(self, name, profession, health):
        self.name = name
        self.profession = profession
        self.health = health
    
    # passive functions
    def add_health(self, bonus_health):
        self.health = self.health + bonus_health
    
    def new_spell(self, new_spell, type, points):
        self.spells[new_spell] = [type, points]

    #  action functions
    def damage(self, damage_received):
        self.health = self.health - damage_received