import items
from random import choice

class Random_Inventory():
    def randomise_inventory(self, num):
        random_list = []
        available_items = [items.Berries(), items.CrustyBread(), items.GrannySmithApple()]

        for i in range(num):
            random_item = choice(available_items)
            random_list.append(random_item)

        return random_list