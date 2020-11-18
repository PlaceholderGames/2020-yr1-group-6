import items
import randomise

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name

class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader1"
        self.gold = 100
        self.inventory = randomise.Random_Inventory.randomise_inventory(None, 5)
        self.inventory.append(items.HealingPotion)