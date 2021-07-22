class Character:
    name = ""
    health = 10
    spells = {
        "" : ["heal", 0],
        "" : ["attack", 0]
    }

    def __init__(self, name, health, spells):
        player_spells = dict(spells)
        self.name = name
        self.health = health
        self.spells = player_spells

    def add_health(self, bonus_health):
        self.health = self.health + bonus_health

    def damage(self, damage_received):
        self.health = self.health - damage_received
    
    def new_spell(self, name, type, points):
        self.spells[name] = [type, points]
    
    def forget_spell(self, spell):
        del self.spells[spell]

# need to remove professions
# class Profession:
    # title = ""
    # health = 0
    # spells = {
    #     "Potion" : ["heal", 5],
    #     "Punch" : ["attack", 2]
    # }

    # def __init__(self, title, health, default_spells):
    #     self.title = title
    #     self.health = health
    #     self.spells = default_spells