from player import Player
from switch import Switch
from collections import OrderedDict
import world

switch = Switch()

#def switch(case):
    #switcher = {
        #"N": player.move_north(),
        #"S": player.move_south(),W
        #"E": player.move_east(),
        #"W": player.move_west()
        #"I": player.print_inventory()
        
    #}
    #func = switcher.get(case, lambda: "Invalid Command")
    #return func()
    #return switcher.get(case, lambda: "Invalid Command")


def play():
    print("Nameless Eldritch")
    world.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        #player.health = player.health
        #game is changing player.health but not updating it globally to be used in switch
        #add a code here to call something from world to add to the health
        if player.is_alive() and not player.victory:
            action_input = choose_action(room, player)
        elif not player.is_alive():
            print("Through all you hard work, it seems it was all for nought.")
        #action_input = get_player_command()
        #action_input = action_input.upper() 
        print(action_input)#Takes any input and converts it to upper case
        
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

def get_player_command():
    return input("Action: ")

def get_available_actions(room, player):
    actions = OrderedDict()

    print("Choose an action: ")

    if player.inventory:
        action_adder(actions, 'I', player.print_inventory, "Print inventory")

    if isinstance(room, world.TraderTile):
        action_adder(actions, 'T', player.trade, "Trade")

    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'A', player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'N', player.move_north, "Go north")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 'S', player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'E', player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'W', player.move_west, "Go west")
    if player.health < 100:
        action_adder(actions, 'H', player.heal, "Heal")

    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))

def choose_action(room, player):
    action = None
    
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)

        if action:
            return action()
        else:
            print("Invalid Action!")
play()