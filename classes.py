class Character:
    name = ""
    health = 0
    spells = {
        "" : ["heal", 0],
        "" : ["attack", 0]
    }

    def __init__(self, name, health, spells):
        self.name = name
        self.health = health
        self.spells = dict(spells)

    def set_name(self, name):
        self.name = name

    def add_health(self, bonus_health):
        self.health = self.health + bonus_health

    def damage(self, damage_received):
        self.health = self.health - damage_received
    
    def new_spell(self, name, type, points):
        self.spells[name] = [type, points]
    
    def forget_spell(self, spell):
        del self.spells[spell]
