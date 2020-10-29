from player import Player
from switch import Switch
import world
player = Player()
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

    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        #player.health = player.health
        #game is changing player.health but not updating it globally to be used in switch
        #add a code here to call something from world to add to the health
        action_input = get_player_command()
        action_input = action_input.upper() 
        print(action_input)#Takes any input and converts it to upper case
        
        if action_input in ["I", "A", "H"]:
            switch.switcher(action_input, player)# The health in switch is different to player
        else:
            player.x, player.y = switch.switcher(action_input, player)
        


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

play()