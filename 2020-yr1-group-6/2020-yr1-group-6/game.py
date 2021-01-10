import pygame
#from pygame import mixer
from enum import Enum

from player import Player
from switch import Switch
from collections import OrderedDict
import world

import graphics

from pygame.locals import *

pygame.font.init()

myfont = pygame.font.SysFont('Times New Roman', 30)
                 
pygame.init()
pygame.display.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

underswitch = False

#pygame.mixer.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Nameless Eldritch") 

clock = pygame.time.Clock()

screen.fill((0, 0, 0))


class GameState:
    NONE = 0
    RUNNING = 1
    QUIT = 2

class LevelState:
    STREET = 0
    SEWER = 1

    
class Game:
    def __init__(self,screenWindow):
        self.screen = screenWindow
        self.status = GameState.NONE
        self.level = LevelState.STREET
        self.keyPressed = None
        self.underswitch = None
        self.levelcheck = False
        
    def start(self):
        #self.initPlayerModel()
        self.status = GameState.RUNNING

    def update(self):
        screen.fill((0, 0, 0))
        self.handleEvents()
        #self.initPlayerModel()
        #if player.levelflag == 2:
            #self.level = LevelState.SEWER
            #player.levelflag = 0
        self.updateMap()
        #self.updateScreen()
        if player.is_alive() and not player.victory:
            self.chooseAction(self.room, player)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #self.status = GameState.QUIT
                pygame.quit()
                quit()


            elif event.type == pygame.KEYDOWN:
                self.keyPressed = None
                if event.key == pygame.K_ESCAPE:
                    self.status = GameState.QUIT
                #elif event.key == pygame.K_n:
                 #   print('Player chose N')
                 #   self.keyPressed = "N"
                #elif event.key == pygame.K_s:
                 #   print('Player chose S')
                 #   self.keyPressed = "S"
                #elif event.key == pygame.K_e:
                    #print('Player chose E')
                    #self.keyPressed = "E"
                #elif event.key == pygame.K_w:
                   # print('Player chose W')
                   # self.keyPressed = "W"
               # elif event.key == pygame.K_i:
                   # print('Player chose I')
                    #self.keyPressed = "I"
                #else:
                   # print('Invalid option chosen')

    def updateMap(self):

        if player.is_alive() and not player.victory:
 
            self.room = world.tile_at(player.x, player.y, underswitch)
            #room.modify_player(player)
            if self.room.x == 1 and self.room.y == 0 :
                self.room.modify_player(player)
            print(self.room.intro_text(self.level))
            self.room.modify_player(player)
            #action_input = Game.choose_action(self.room, player)
        elif not player.is_alive():
            print("Through all you hard work, it seems it was all for nought.")
            game.status = GameState.QUIT

    def updateScreen(self):
        screen.fill((255, 0, 255))
        textsurface = myfont.render(self.keyPressed, False, (0, 0, 0))
        screen.blit(textsurface,(0,0))
    
    def initPlayerModel(self):
        self.player_model = graphics.Player([0, 5])
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player_model)

        for entity in self.all_sprites:
            screen.blit(entity.surf, entity.rect)

    def under_switch_true():
        #global underswitch 
        self.underswitch = True


    def under_switch_false():
        #global underswitch 
        self.underswitch = False #If underswitch is not working, uncomment code


    def get_available_actions(room, player):
        actions = OrderedDict()
    

        print("Choose an action: ")

        if player.inventory:
            Game.action_adder(actions, 'I', player.print_inventory, "Print inventory")

        if isinstance(room, world.TraderTile):
            Game.action_adder(actions, 'T', player.trade, "Trade")

        if isinstance(room, world.EnemyTile1 or world.EnemyTile2 or world.EnemyTile3) and room.enemy.is_alive():
            Game.action_adder(actions, 'A', player.attack, "Attack")
            Game.action_adder(actions, 'R', player.flee, "Run")
            Game.action_adder(actions, 'H', player.heal, "Heal")
        elif isinstance(room, world.EnemyTile2) and room.enemy.is_alive():
            Game.action_adder(actions, 'A', player.attack, "Attack")
            Game.action_adder(actions, 'R', player.flee, "Run")
            Game.action_adder(actions, 'H', player.heal, "Heal")
        elif isinstance(room, world.EnemyTile3) and room.enemy.is_alive():
            Game.action_adder(actions, 'A', player.attack, "Attack")
            Game.action_adder(actions, 'R', player.flee, "Run")
            Game.action_adder(actions, 'H', player.heal, "Heal")
        elif isinstance(room, world.EnemyTile4) and room.enemy.is_alive():
            Game.action_adder(actions, 'A', player.attack, "Attack")
            Game.action_adder(actions, 'R', player.flee, "Run")
            Game.action_adder(actions, 'H', player.heal, "Heal")
        else:
            #if not underswitch:
                #Game.action_adder(actions, 'U', Game.under_switch_true, "Go to the underworld")
            #elif underswitch:
                #Game.action_adder(actions, 'U', Game.under_switch_false, "Go back to the real world")
            if world.tile_at(room.x, room.y - 1, underswitch):
                Game.action_adder(actions, 'N', player.move_north, "Go north")
            if world.tile_at(room.x, room.y + 1, underswitch):
                Game.action_adder(actions, 'S', player.move_south, "Go south")
            if world.tile_at(room.x + 1, room.y, underswitch):
                Game.action_adder(actions, 'E', player.move_east, "Go east")
            if world.tile_at(room.x - 1, room.y, underswitch):
                Game.action_adder(actions, 'W', player.move_west, "Go west")
        
            if player.health < 100:
                Game.action_adder(actions, 'H', player.heal, "Heal")

            if isinstance(room, world.PuzzleTile) and not room.solved():
                Game.action_adder(actions, 'P', player.answer_puzzle, "Answer the puzzle" )
            
            if isinstance(room, world.PuzzleTile2) and not room.solved():
                Game.action_adder(actions, 'P', player.answer_puzzle, "Answer the puzzle" )
                del actions['N']
            elif isinstance(room, world.PuzzleTile2) and room.solved():
                Game.action_adder(actions, 'N', player.move_north, "Go north")

            if isinstance(room, world.PuzzleTile3) and not room.solved():
                Game.action_adder(actions, 'P', player.answer_puzzle, "Answer the puzzle" )
                del actions['N']
            elif isinstance(room, world.PuzzleTile3) and room.solved():
                Game.action_adder(actions, 'N', player.move_north, "Go north")


        return actions

    def action_adder(action_dict, hotkey, action, name, *args):
        action_dict[hotkey.lower()] = action
        action_dict[hotkey.upper()] = action
        print("{}: {}".format(hotkey, name))

    def chooseAction(self, room, player):
        action = None
        
        while not action:
            available_actions = Game.get_available_actions(room, player)
            action_input = input("Action: ")
            action_input = action_input.upper()
            action = available_actions.get(action_input)

            if action_input == 'N' or action_input == 'E' or action_input == 'S' or action_input == 'W':
                player.last_action = action_input
            
            if action_input == 'A':
                return action(underswitch)
            elif action_input == 'P':
                return action(underswitch)
            elif action_input == 'T':
                return action(underswitch)
            elif action_input == 'R':
                return action(underswitch)
            elif action_input != 'A' and action_input in available_actions :
                #screen.fill((255,0,255))
                return action()
            else: #action_input != available_actions:
                print("Invalid Action!")
        
game = Game(screen)
game.start()
world.parse_world_dsl(game.level)
#world.parse_world_under_dsl()
player = Player()
game.updateScreen()
#screen.fill((0, 0, 0))

while game.status == GameState.RUNNING:
    #pygame.mixer.music.load("Audio/Game Audio Files/Zone1/nw-bg1.ogg")
    #pygame.mixer.music.play(loops=-1)
    #pygame.mixer.music.set_volume(0.1)
    if player.levelflag == 2:
            game.level = LevelState.SEWER
            player.levelflag = 0
    if game.level == LevelState.SEWER and not game.levelcheck:
        world.world_map = []
        world.parse_world_dsl(game.level)
        player.x = world.start_tile_location[0]
        player.y = world.start_tile_location[1]
        #world.parse_world_dsl(game.level)
        game.levelcheck = True
    pygame.event.pump()
    game.update()
    pygame.display.flip()
    clock.tick(60)
    
if game.status == GameState.QUIT:
    pygame.quit()

#background = graphics.Street([0, 0])
#zone1 = pygame.sprite.Group()
#zone1.add(background)
#player_model = graphics.Player()
#all_sprites = pygame.sprite.Group()
#all_sprites.add(player_model)


#def play():
#    print("Nameless Eldritch")
 #   pygame.mixer.music.load("Audio/Game Audio Files/Zone1/nw-bg1.ogg")
  #  pygame.mixer.music.play(loops=-1)
   # pygame.mixer.music.set_volume(0.1)
    #world.parse_world_dsl()
#
 #   player = Player()
  #  
   # while player.is_alive() and not player.victory:
#
        #for event in pygame.event.get():
           # if event.type == KEYDOWN:
               # if event.key == K_ESCAPE:
                 #   quit
           # elif event.type == QUIT:
              #  quit
        
        #screen.fill((0, 0, 0))
       # for entity in zone1:
        #    screen.blit(entity.surf, entity.rect)
        #for entity in all_sprites:
         #   screen.blit(entity.surf, entity.rect)
            
       # pygame.display.flip()
        #clock.tick(30)

 #       room = world.tile_at(player.x, player.y, underswitch)
  #      room.modify_player(player)
   #     print(room.intro_text())
        

    #    if player.is_alive() and not player.victory:
     #       action_input = choose_action(room, player)
      #  elif not player.is_alive():
       #     print("Through all you hard work, it seems it was all for nought.")
        #action_input = get_player_command()
        #action_input = action_input.upper() 
        #print(action_input)#Takes any input and converts it to upper case
        
 #       if action_input in ["I", "A", "H"]:
  #          switch.switcher(action_input, player)# The health in switch is different to player
   #     else:
    #        player.x, player.y = switch.switcher(action_input, player)
        


    #if action_input == "N" :
        #player.move_north()
    #elif action_input == "S":
        #player.move_south()
    #elif action_input == "E":
        #player.move_east()
    #elif action_input == "W":
       # plater.move_west()
    #else:
        #print("Invalid Action")


#play()

