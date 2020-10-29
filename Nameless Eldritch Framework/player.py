import items
import world

class Player:
    def __init__(self):
        self.inventory = [items.RustySword(), items.Rock(), items.Dagger(), items.Gold(5), items.CrustyBread(), items.GrannySmithApple()]

        self.x = 1
        self.y = 2
        self.health = 100


    def __str__(self):
        return self.health

    def move(self, dx, dy):
        self.x += dx 
        self.y += dy 

    def move_north(self):
        self.move(dx = 0, dy = -1)
        return (self.x, self.y)

    def move_south(self):
        self.move(dx = 0, dy = 1)
        return (self.x, self.y)

    def move_east(self):
        self.move(dx = 1, dy = 0)
        return (self.x, self.y)

    def move_west(self):
        self.move(dx = -1, dy = 0)
        return (self.x, self.y)

    def print_inventory(self):
        print("Inventory: \n")
        
        for item in self.inventory:
            print(str(item))
        
        best_weapon = self.most_powerful_weapon()

        print("Your best weapon is your {}".format(best_weapon))

        return

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None

        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item.name
                    max_damage = item.damage
            except AttributeError:
                pass

        return (best_weapon, max_damage)

    def attack(self):
        best_weapon, max_damage = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy

        print("You use {} against {}!".format(best_weapon, enemy.name))
        enemy.health -= max_damage

        if not enemy.is_alive():
            print("You've killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.health))
    
    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]

        if not consumables:
            print("You don't have any consumables to heal with!")
            return
        
        print("Choose an item to use to heal: ")
        for i, item in enumerate(consumables, 1):
            
            print("{}. {}".format(i, item))

        valid = False

        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.health = min(100, self.health + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.health))
                valid = True
            except (ValueError, IndexError):
                print("Invaild Choice, try again.")
        return self.health