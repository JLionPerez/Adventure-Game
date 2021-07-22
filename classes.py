class Character:
    name = ""
    profession = ""
    health = 0
    spells = {
        "" : ["heal", 0],
        "" : ["attack", 0]
    }

    def __init__(self, Profession, name):
        player_spells = dict(Profession.spells)
        self.name = name
        self.profession = Profession.title
        self.health = Profession.health
        self.spells = player_spells

    def add_health(self, bonus_health):
        self.health = self.health + bonus_health

    def damage(self, damage_received):
        self.health = self.health - damage_received
    
    def new_spell(self, new_spell, type, points):
        self.spells[new_spell] = [type, points]
    
    def forget_spell(self, spell):
        del self.spells[spell]

# need to remove professions
class Profession:
    title = ""
    health = 0
    spells = {
        "Potion" : ["heal", 5],
        "Punch" : ["attack", 2]
    }

    def __init__(self, title, health, default_spells):
        self.title = title
        self.health = health
        self.spells = default_spells