import random
import player
import enemies
import npc



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

class BoringTile(MapTile):
    def intro_text(self):
        return """
        This is a very dull part of the city, nothing
        of interest here
        """

class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True
    def intro_text(self):
        return """
        You have grown weary but you 
        finally see a sign in the distance...
        It reads "Now Entering Aurora", 
        finally you are out of the city!
        """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()

        if r < 0.50:
            self.enemy = enemies.Placeholder1_Enemy()
            self.alive_text = "General entry description"
            self.death_text = "General death description"
        elif r < 0.80:
            self.enemy = enemies.Placeholder2_Enemy()
            self.alive_text = "General entry description"
            self.death_text = "General death description"
        else:
            self.enemy = enemies.Placeholder3_Enemy()
            self.alive_text = "General entry description"
            self.death_text = "General death description"

        super().__init__(x, y)

    def intro_text(self):
        alive_intro_text = self.alive_text
        death_exit_text = self.death_text
        print(alive_intro_text)
        if self.enemy.is_alive():
            return "A {} awaits!".format(self.enemy.name)
        else:
            return "You've defeated the {}. \n".format(self.enemy.name) + death_exit_text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.health = player.health - self.enemy.damage#Health here isn't updating
            #Player health isn't updating after healing
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

tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "BT": BoringTile,
                  "TT": TraderTile,
                  "FG": FindGoldTile,
                  "  ": None}

world_dsl = """
|  |VT|  |
|  |FG|  |
|EN|FG|TT|
|  |ST|  |
"""



world_map = []
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

def tile_at(x, y):# These x and y are not updating
    if x < 0 or y < 0:
        return None
    
    try:
        return world_map[y][x]
    except IndexError:
        return None