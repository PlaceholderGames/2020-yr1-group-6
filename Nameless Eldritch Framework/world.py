import random
import player
import enemies



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
    def intro_text(self):
        return """
        You have grown weary but you finally see a sign in the distance...
        It reads "Now Entering Aurora", finally you are out of the city!
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

world_map = [
    [None,VictoryTile(1,0), None],
    [None,BoringTile(1,1), None],
    [EnemyTile(0,2),StartTile(1,2),EnemyTile(2,2)],
    [None,EnemyTile(1,3),None]
]

def tile_at(x, y):# These x and y are not updating
    if x < 0 or y < 0:
        return None
    
    try:
        return world_map[y][x]
    except IndexError:
        return None