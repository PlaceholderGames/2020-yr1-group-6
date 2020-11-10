import random
import player
import enemies
import npc
import items



class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in the middle of a big city with horrors
        in the sky.
        You can make out four paths, all equally filled with monsters and fire.
        """

class StatueTile(MapTile):
    def intro_text(self):
        return """
        A strong looking statue stands blocking the way.
        It looks like it has some energy inside.
        Maybe in another world this was a strong foe.
        """

class VictoryTile(MapTile):
    def __init__(self, x, y):
        self.key_check = False
        super().__init__(x, y)


    def modify_player(self, player):
        for items in player.inventory:
            if items.name == "Crooked Key":
                self.key_check = True
                player.victory = True
    def intro_text(self):
        #solved = PuzzleTile.solved
        
        if self.key_check == True:
            return """
            You use the small key on the gate, and it opens!
            You have grown weary but you 
            finally see a sign in the distance...
            It reads "Now Entering Aurora", 
            finally you are out of the city!
            """
        else:
            return """
            You find a locked gate with a sign outsde.
            It looks like a small key may open the gate.
            For now there is nothing you can do
            """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        #r = random.random()
        

        #if r < 0.50:
           # self.enemy = enemies.Rat()
           # self.alive_text = self.enemy.description
            #self.death_text = "General death description"
        #elif r < 0.80:
           # self.enemy = enemies.Plant()
            #self.alive_text = self.enemy.description
            #self.death_text = "General death description"
        #else:
        self.enemy = enemies.Knight()
        self.alive_text = self.enemy.description
        self.death_text = "I wish to take hounour in death."

        super().__init__(x, y)

    def intro_text(self):
        alive_intro_text = self.alive_text
        death_exit_text = self.death_text
        print(alive_intro_text)
        if self.enemy.is_alive():
            print("A {} awaits!".format(self.enemy.name))
            return "{} has {} health.".format(self.enemy.name, self.enemy.health)
        else:
            return "You've defeated the {}. \n".format(self.enemy.name) + death_exit_text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.health = player.health - self.enemy.damage
            print("{} does {} damage. You have {} HP remaining.".format(self.enemy.name, self.enemy.damage, player.health))
            return player.health

class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def intro_text(self):
        return"""
        Hunkered down in this small shelter, you 
        see a frail creature with a stand, with a vairety of goods.
        They looking willing to trade with you.
        """

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            user_input = user_input.upper()
            if user_input == 'Q':
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid Choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
            
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
            
        print("Trade Complete!")

    def check_if_trade(self, player):
        while True:
            print("Would you like to Buy, Sell, or Quit?")
            user_input = input()
            user_input = user_input.upper()

            if user_input == 'Q':
                return
            elif user_input == 'B':
                print("Here's whats available to buy today: ")
                self.trade(buyer = player, seller = self.trader)
            elif user_input == 'S':
                print("What are you willing to part with today?: ")
                self.trade(buyer = self.trader, seller = player)
            else:
                print("Invalid choice! (Use B, S, or Q)")

class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1,50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))
    
    def intro_text(self):
        if self.gold_claimed:
            return """
            Nothing of note in this part of the street.
            You must continue on with your search.
            """
        else:
            return """
            You find a rotting corpse, with a certain shine
            emitting from it. After further investigation you
            find some gold!
            """

class PuzzleItemTile1(MapTile):
    def __init__(self, x, y):
        #self.inventory = [items.DigitNote1, items.DigitNote2]
        self.note_1_claimed = False
        super().__init__(x, y)
    
    def modify_player(self, player):
        if not self.note_1_claimed:
            self.note_1_claimed = True
            player.inventory.append(items.DigitNote1())
            #self.inventory.remove(self.inventory[0])

    def intro_text(self):
        if self.note_1_claimed == True:
            return """
            There's nothing of interest left here, 
            look elsewhere in the street.
            """
        else:
            return """
            You find a torn peice of paper stuck on a wall.
            You pick it up and it has a number and a symbol on it.
            This might be useful later on.
            """

class PuzzleItemTile2(MapTile):
    def __init__(self, x, y):
        #self.inventory = [items.DigitNote1, items.DigitNote2]
        self.note_2_claimed = False
        super().__init__(x, y)
    
    def modify_player(self, player):
        if not self.note_2_claimed:
            self.note_2_claimed = True
            player.inventory.append(items.DigitNote2())
            #self.inventory.remove(self.inventory[0])

    def intro_text(self):
        if self.note_2_claimed == True:
            return """
            There's nothing of interest left here, 
            look elsewhere in the street.
            """
        else:
            return """
            You find a torn peice of paper attached to a rotting corpse.
            You pick it up and it has a number and a symbol on it.
            This might be useful later on.
            """

class PuzzleTile(MapTile):
    def __init__(self, x, y):
        self.puzzle_solved = False
        super().__init__(x, y)
        

    def intro_text(self):
        if self.puzzle_solved == True:
            return """
            An empty box lies here, look around and
            you might be able to use the key somewhere!
            """
        else:
            return """
            You find a locked box beneath your feet.
            It has a Triangle, Circle and a Square,
            with number dials underneath. 
            You might be able to open it if you know the code.
            """

    def solved(self):
        return self.puzzle_solved



tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "SU": StatueTile,
                  "TT": TraderTile,
                  "FG": FindGoldTile,
                  "P1": PuzzleItemTile1,
                  "P2": PuzzleItemTile2,
                  "PT": PuzzleTile,
                  "  ": None}

world_dsl = """
|P2|VT|  |
|P1|PT|  |
|SU|FG|TT|
|  |ST|  |
"""

world_under_dsl = """
|  |  |  |
|  |FG|  |
|EN|FG|TT|
|  |FG|  |
"""

world_map = []
world_undermap = []
#world_map = [
   # [None,VictoryTile(1,0), None],
  #  [None,BoringTile(1,1), None],
   # [EnemyTile(0,2),StartTile(1,2),EnemyTile(2,2)],
  #  [None,EnemyTile(1,3),None]
#]

start_tile_location = None

def parse_world_dsl():
    #if not is_dsl_valid(world_dsl):
    #    raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]

        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)

def parse_world_under_dsl():
    #if not is_dsl_valid(world_dsl):
    #    raise SyntaxError("DSL is invalid!")

    dsl_lines = world_under_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]

        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            row.append(tile_type(x, y) if tile_type else None)

        world_undermap.append(row)


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    
    lines = dsl.splitlines()
    line = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]

    for count in pipe_counts:
        if count != pipe_counts[1]:
            return False
    
    return True

def tile_at(x, y, underswitch):
    if x < 0 or y < 0:
        return None
    
    if not underswitch:
        try:
            return world_map[y][x]
        except IndexError:
            return None
    elif underswitch:
        try:
            return world_undermap[y][x]
        except IndexError:
            return None