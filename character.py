import profession

class Character:
    # default variables
    name = ""
    profession = ""
    health = 10
    items = []

    # constructor
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
    
    # passive functions
    def add_health(self, bonus_health):
        self.health = self.health + bonus_health
    
    def add_defense(self, defense):
        self.defense = defense

    def add_energy(self, bonus_energy):
        self.energy = self.energy + bonus_energy
    
    def new_attack(self, new_attack, damage):
        self.attacks[new_attack] = damage

    #  action functions
    def damage(self, damage_received):
        self.health = self.health - damage_received

class Profession:
    # default variables
    profession_name = ""
