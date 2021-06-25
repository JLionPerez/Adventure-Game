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
    def __init__(self, Profession, name):
        self.name = name
        self.profession = Profession.profession_title
    
    # passive functions
    def add_health(self, bonus_health):
        self.health = self.health + bonus_health
    
    def new_spell(self, new_spell, type, points):
        self.spells[new_spell] = [type, points]

    #  action functions
    def damage(self, damage_received):
        self.health = self.health - damage_received

class Profession:
    # default variables
    profession_title = ""
    health = 0
    spells = {
        "Light Heal" : ["heal", 5],
        "Burn" : ["attack", 2],
        "Frost" : ["attack", 3]
    }

    def __init__(self, title, health):
        self.profession_title = title
        self.health = health

    def set_profession(self, profession):
        self.profession_title = profession

ob1 = Profession("Thief", 30)
ob2 = Character(ob1, "Mary")
print (ob2.profession)
