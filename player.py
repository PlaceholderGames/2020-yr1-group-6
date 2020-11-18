import items
import world
import graphics

player_model = graphics.Player()

class Player:
    def __init__(self):
        self.inventory = [items.RustySword(), 
                        items.Rock(), 
                        items.Dagger(), 
                        items.CrustyBread(), 
                        items.GrannySmithApple()]

        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.health = 100
        self.gold = 5
        self.victory = False

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return self.health

    def move(self, dx, dy):
        self.x += dx 
        self.y += dy 

    def move_north(self):
        self.move(dx = 0, dy = -1)
        player_model.update("N")
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

    def answer_puzzle(self, underswitch):
        room = world.tile_at(self.x, self.y, underswitch)
        if not room.solved():
            action_input = input("Answer: ")

            if action_input != ("369"):
                print("Incorrect Answer, try again")
            else:
                print("The box opens up to reveal a key, you pick it up")
                self.inventory.append(items.Key())
                room.puzzle_solved = True

                

    def print_inventory(self):
        print("Inventory: \n")
        
        for item in self.inventory:
            print(str(item))
        print("Gold: {}".format(self.gold))
        
        best_weapon, max_damage = self.most_powerful_weapon()

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

    def attack(self, underswitch):
        weapons = [item for item in self.inventory if isinstance(item, items.Weapon)]
        choice = input("Would you like use your most powerful weapon?(Y/N)")
        choice = choice.upper()
        if choice == "Y":
            weapon, max_damage = self.most_powerful_weapon()
        else:
            if not weapons:
                print("You have no weapons to fight with!")
                return

            print("Choose your weapon to fight with:")

            for i, item in enumerate(weapons, 1):
                print("{}. {}".format(i, item))
            
            valid = False

            while not valid:
                numchoice = input("")
                try:
                    chosenweapon = weapons[int(numchoice) -1]
                    print("Your weapon of choice is {}".format(chosenweapon.name))
                    valid = True
                except (ValueError, IndexError):
                    print("Invaild choice, try again.")
            
                try:
                    weapon = chosenweapon.name
                    max_damage = chosenweapon.damage
                except AttributeError:
                    pass
            
        room = world.tile_at(self.x, self.y, underswitch)
        enemy = room.enemy

        print("You use {} against {}!".format(weapon, enemy.name))
        enemy.health -= max_damage

        if not enemy.is_alive():
            print("You've killed {}!".format(enemy.name))
            self.gold = self.gold + enemy.gold
            enemy.gold -= enemy.gold
            self.inventory.extend(enemy.inventory)
            enemy.inventory = None
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
                print("Invaild choice, try again.")
        return self.health

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

    