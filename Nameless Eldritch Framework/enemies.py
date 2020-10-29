class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.health > 0

class Placeholder1_Enemy(Enemy):
    def __init__(self):
        self.name = "Placeholder1"
        self.health = 25
        self.damage = 10

class Placeholder2_Enemy(Enemy):
    def __init__(self):
        self.name = "Placeholder2"
        self.health = 50
        self.damage = 30

class Placeholder3_Enemy(Enemy):
    def __init__(self):
        self.name = "Placeholder3"
        self.health = 80
        self.damage = 50