import random
import player
import enemies
import npc
import items



class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def intro_text(self, level):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

class StartTile(MapTile):
    def intro_text(self, level):
        if level == 0:
            return """
            You find yourself in the middle of a big city with horrors
            in the sky.
            You can make out four paths, all equally filled with monsters and fire.
            """
        elif level == 1:
            return """
            Finally out of the open, you find yourself
            in a dark, damp sewer. It looks very narrow
            and you can't see all that well, however
            you decide to continue on your way
            """

class EmptyTile(MapTile):
    def __init__(self, x, y):
       self.r = 0
       super().__init__(x, y)

    def modify_player(self, player):
        self.r = random.randint(-1, 2)


    def intro_text(self, level):
        if level == 0:
            if self.r == 0:
                return """
                You look around the street to see it 
                infested with subhuman creatures,
                feral and dangerous.
                You muster the courage to forward on with
                your search of a way out of this nightmare.
                """
            elif self.r == 1:
                return """
                The longer you spend exploring the streets,
                the more uneasy you begin to feel.
                Never the less, you continue onwards.
                """
            elif self.r == 2:
                return """
                The more you explore, the feeling of
                needing to arm yourself grows. Having
                some type of weapon may come in handy.
                """
        elif level == 1:
            if self.r == 0:
                return """
                The longer you spend in the sewer, the harder the smell
                is to overcome. On the brightside, your eyes
                seem to finally be adjusting to the darkness.
                """
            elif self.r == 1:
                return """
                You begin to feel more familiar with the layout
                of this sewer system, the design seems to suggest a way out,
                you keep exploring in hopes to escape.
                """
            elif self.r == 2:
                return """
                The more you explore, the more you think
                about what could be hidden in such a place.
                Maybe if you look around enough, you may
                find something useful to your fight.
                """

class StatueTile(MapTile):
    def intro_text(self, level):
        return """
        A strong looking statue stands blocking the way.
        It looks like it has some energy inside.
        Maybe in another world this was a strong foe.
        """

class VictoryTile(MapTile):
    def __init__(self, x, y):
        self.key_check = False
        self.vicflag = False
        super().__init__(x, y)


    def modify_player(self, player):
        for items in player.inventory:
            if items.name == "Crooked Key":
                self.key_check = True
                #player.victory = True
                player.levelflag = player.levelflag + 1
        if self.vicflag == True:
            player.victory = True
    def intro_text(self, level):
        #solved = PuzzleTile.solved
        if level == 0:
            if self.key_check == True:
                return """
                You use the small key on the gate, and it opens!
                It seems to lead into a sewer system. You decide
                to take shelter in the sewer. You might find something
                to explain everything that is going on if you keep on going.
                """
            else:
                return """
                You find a locked gate that leads into the sewer.
                It looks like a small key may open the gate.
                For now there is nothing you can do.
                """
        elif level == 1:
            self.vicflag = True
            return """
            You managed to find a way out the
            sewer system with your life.
            You brace yourself for the outside
            world again and venture forth.
            """

class EnemyTile1(MapTile):
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

    def intro_text(self, level):
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

class EnemyTile2(MapTile):
    def __init__(self, x, y):
        self.enemy = enemies.Rat()
        self.alive_text = self.enemy.description
        self.death_text = "Fades out of pure spite, leaving nothing behind."

        super().__init__(x, y)

    def intro_text(self, level):
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

class EnemyTile3(MapTile):
    def __init__(self, x, y):
        self.enemy = enemies.Plant()
        self.alive_text = self.enemy.description
        self.death_text = "The pricks on the plant fall off, one by one until nothing remains."

        super().__init__(x, y)

    def intro_text(self, level):
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

class EnemyTile4(MapTile):
    def __init__(self, x, y):
        self.enemy = enemies.Goblin()
        self.alive_text = self.enemy.description
        self.death_text = "The goblin melts into a pool of gunk, leaving all of their items behind."

        super().__init__(x, y)

    def intro_text(self, level):
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

    def intro_text(self, level):
        if level == 0:
            return"""
            Hunkered down in this small shelter, you 
            see a frail creature with a stand, with a vairety of goods.
            They looking willing to trade with you.
            """
        elif level == 1:
            return """
            Hidden away in what seems to be a hole,
            hand carved into the brick walls of the sewer,
            you spot a small, bug eyed creature. It may
            be willing to trade with you.
            """

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            if item.value != 0:
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


class FindWeaponTile(MapTile):
    def __init__(self, x, y):
        self.weapon_claimed = False
        self.weapon = items.Rock()
        super().__init__(x, y)
    
    def modify_player(self, player):
        if not self.weapon_claimed:
            self.weapon_claimed = True
            player.inventory.append(items.Rock())
            print("{} added to inventory.".format(self.weapon.name))

    def intro_text(self, level):
        if self.weapon_claimed:
            return """
            Nothing remains here except some
            scattered rubbish. Maybe I should try
            to find a use for this rock?
            """
        else:
            return """
            After examining the area,
            you find a large rock, it might be worth taking
            to be used as a weapon.
            """

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
    
    def intro_text(self, level):
        if level == 0:
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
        elif level == 1:
            if self.gold_claimed:
                return """
                You feel a sense of deja vu looking around,
                however there no longer seems to be anything
                of use here. You should continue on
                """
            else:
                return """
                You find a group of dead rats, but the longer
                you investigate, it seems to have some more
                gold in the center!
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

    def intro_text(self, level):
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

    def intro_text(self, level):
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
        

    def intro_text(self, level):
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

class PuzzleTile2(MapTile):
    def __init__(self, x, y):
        self.puzzle_solved = False
        super().__init__(x, y)
        

    def intro_text(self, level):
        if self.puzzle_solved == True:
            return """
            The door opens open to show
            even more sewerage. You decide to continue on.
            """
        else:
            return """
            You find a locked door with a keypad next to it.
            It has the numbers 1, 6, 7, and 3 on it.
            You might be able to open it if you know the code.
            """

    def solved(self):
        return self.puzzle_solved

class PuzzleTile3(MapTile):
    def __init__(self, x, y):
        self.puzzle_solved = False
        super().__init__(x, y)
        

    def intro_text(self, level):
        if self.puzzle_solved == True:
            return """
            The door opens open to show
            an exit out of the sewer. You decide to make your way
            towards the exit.
            """
        else:
            return """
            You find a locked door with a keypad next to it.
            It has the numbers 4, 3, 8, and 9 on it.
            You might be able to open it if you know the code.
            """

    def solved(self):
        return self.puzzle_solved

class PuzzleItemTile3(MapTile):
    def __init__(self, x, y):
        self.code_claimed = False
        super().__init__(x, y)
    
    def modify_player(self, player):
        if not self.code_claimed:
            self.code_claimed = True
            player.inventory.append(items.SewerCode())

    def intro_text(self, level):
        if self.code_claimed == True:
            return """
            There's nothing of interest left here, 
            maybe find a place to use this clue.
            """
        else:
            return """
            You find a set of numbers etched into the
            sewer wall. You write it down on a peice of scrap paper.
            This might be useful later on.
            """

class PuzzleItemTile4(MapTile):
    def __init__(self, x, y):
        self.code_claimed = False
        super().__init__(x, y)
    
    def modify_player(self, player):
        if not self.code_claimed:
            self.code_claimed = True
            player.inventory.append(items.SewerCode2())

    def intro_text(self, level):
        if self.code_claimed == True:
            return """
            There's nothing of interest left here, 
            maybe find a place to use this clue.
            """
        else:
            return """
            You find a set of numbers etched into the
            sewer wall. You write it down on a peice of scrap paper.
            This might be useful later on.
            """

class FindHealthTile(MapTile):
    def __init__(self, x, y):
        self.health_claimed = False
        self.item = items.HealingPotion()
        super().__init__(x, y)
    
    def modify_player(self, player):
        if not self.health_claimed:
            self.health_claimed = True
            player.inventory.append(items.HealingPotion())
            print("{} added to inventory.".format(self.item.name))

    def intro_text(self, level):
        if self.health_claimed:
            return """
            All that remains is the stone pedestal,
            in which you took the healing potion.
             You should continue your search.
            """
        else:
            return """
            You find a small room, with a pedestal in
            the center, with a light from the roof
            shining down on it. You get closer and find 
            a healing potion! You decide to take it.
            """



tile_type_dict = {"VT": VictoryTile,
                  "E1": EnemyTile1,
                  "E2": EnemyTile2,
                  "E3": EnemyTile3,
                  "E4": EnemyTile4,
                  "ST": StartTile,
                  "SU": StatueTile,
                  "TT": TraderTile,
                  "FG": FindGoldTile,
                  "P1": PuzzleItemTile1,
                  "P2": PuzzleItemTile2,
                  "P3": PuzzleItemTile3,
                  "P4": PuzzleItemTile4,
                  "PT": PuzzleTile,
                  "SP": PuzzleTile2,
                  "PP": PuzzleTile3,
                  "ET": EmptyTile,
                  "WT": FindWeaponTile,
                  "FH": FindHealthTile,
                  "  ": None}

#world_dsl = """
#|P2|VT|  |
#|P1|PT|  |
#|SU|FG|TT|
#|ET|ST|ET|
#"""

world_dsl = """
|P2|VT|  |  |
|E3|ET|  |  |
|TT|PT|  |  |
|FG|WT|  |  |
|P1|ET|ET|ST|
|ET|FG|ET|ET|
"""

world_under_dsl = """
|  |  |  |
|  |FG|  |
|E1|FG|TT|
|  |FG|  |
"""

world_dsl_2 = """
|  |  |  |FH|  |  |VT|
|  |  |  |ET|  |  |PP|
|  |  |  |E4|ET|ET|ET|
|  |  |  |P4|  |  |ET|
|  |  |  |  |  |  |ET|
|  |  |  |TT|  |  |SP|
|ST|ET|E2|FG|ET|ET|ET|
|  |  |  |  |  |  |ET|
|  |P3|ET|ET|E2|ET|ET|
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

def parse_world_dsl(levelstate):
    #if not is_dsl_valid(world_dsl):
    #    raise SyntaxError("DSL is invalid!")

    if levelstate == 0:
        dsl_lines = world_dsl.splitlines()
        #world_map = []
    elif levelstate == 1:
        dsl_lines = world_dsl_2.splitlines()
        #world_map = []
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