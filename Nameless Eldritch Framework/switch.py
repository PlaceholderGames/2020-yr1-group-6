
class Switch:
    def switcher(self, case, player):
        method_case ='case_' + str(case)
        method = getattr(self, method_case, lambda: "Invalid Command!")
        return method(player)
        
    def case_N(self, player):
        x, y = player.move_north()
        return x, y

    def case_S(self, player):
        x, y = player.move_south()
        return x, y

    def case_E(self, player):
        x, y = player.move_east()
        return x, y

    def case_W(self, player):
        x, y = player.move_west()
        return x, y
    
    def case_I(self, player):
        player.print_inventory()
        return

    def case_A(self, player):
        player.attack()
        return

    def case_H(self, player):
        player.heal()## During battle, player health is updated, but then it is not updated here.
        return
