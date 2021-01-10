import random
import items
import randomise

class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.health > 0

class Rat(Enemy):
    def __init__(self):
        self.name = "Deranged Rat"
        self.description = "A screeching rat runs straight for you. This should be an easy fight"
        self.health = random.randint(20, 30)
        self.damage = random.randint(5, 10)
        self.gold = random.randint(0, 5)
        self.inventory = randomise.Random_Inventory.randomise_inventory(None, 2)


class Plant(Enemy):
    def __init__(self):
        self.name = "Deathly Snapping Plant"
        self.description = "A vicious looking plant with teeth like leaves. Don't get to close to those sharp pricks."
        self.health = random.randint(30, 40)
        self.damage = random.randint(10, 15)
        self.gold = random.randint(10, 35)
        self.inventory = randomise.Random_Inventory.randomise_inventory(None, 3)
        #self.inventory = [items.GrannySmithApple(),
                        #items.Berries()]

class Knight(Enemy):
    def __init__(self):
        self.name = "Consumed Knight"
        self.description = "Once an honourable knight in our world, unmoving and righteous, this knight has been overcome with old eldritch evil"
        self.health = random.randint(40, 60)
        self.damage = random.randint(15, 25)
        self.gold = random.randint(40, 70)
        self.inventory = randomise.Random_Inventory.randomise_inventory(None, 1) 
        self.inventory.append(items.RustySword())
        self.inventory.append(items.DigitNote3())
        #self.inventory = [items.RustySword()]

class Goblin(Enemy):
    def __init__(self):
        self.name = "Deformed Green Goblin"
        self.description = "A small, armoured goblin. He looks prepared for a fight."
        self.health = random.randint(25, 35)
        self.damage = random.randint(30, 40)
        self.gold = random.randint(15, 35)
        self.inventory = randomise.Random_Inventory.randomise_inventory(None, 3)
        #self.inventory = [items.GrannySmithApple(),
                        #items.Berries()]