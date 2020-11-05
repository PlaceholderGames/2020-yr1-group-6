class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")
    
    def __str__(self):
        return self.name + ' - ' + self.description

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")
    
    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)

class AltConsumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw AltConsumable objects.")
    
    def __str__(self):
        return self.name + '(' + str(self.multiplyer) + ')'

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A small rock, suitable for throwing and bludgeoning."
        self.damage = 5
        self.value = 15

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. " \
                            "Somewhat more dangerous than a rock."
        self.damage = 10
        self.value = 50

class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing its age, " \
                            "but it still has some fight left in it."
        self.damage = 20
        self.value = 100

class Gold(AltConsumable):
    def __init__(self, multiplyer):
        self.name = "Gold"
        self.multiplyer = multiplyer
        self.description = "A small gold coin to be traded for services and wares."

class CrustyBread(Consumable):   
    def __init__(self):#, multiplyer):
        self.name = "Crusty Bread"
        #self.multiplyer = multiplyer
        self.description = "A very hard loaf of bread. It looks like it's beginning to gather mold."
        self.healing_value = 5
        self.value = 25

class GrannySmithApple(Consumable):
    def __init__(self):#, multiplyer):
        self.name = "Granny Smith Apple"
        #self.multiplyer = multiplyer
        self.description = "A very sweet granny smith apple. It's glowingly green and looks delicious."
        self.healing_value = 20
        self.value = 40

class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 75