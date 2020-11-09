import pygame

from pygame.locals import (
    RLEACCEL,
    K_w,
    K_s,
    K_a,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("Graphics/Player.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, action):
        if action == "W":
            self.rect.move_ip(0, -5)
        if action == "E":
            self.rect.move_ip(0, 5)
        if action == "N":
            self.rect.move_ip(-5, 0)
        if action == "S":
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Street(pygame.sprite.Sprite):
    def __init__(self, location):
        super(Street, self).__init__()
        self.surf = pygame.image.load("Graphics/Street.png").convert()
        self.surf = pygame.transform.scale(self.surf, (800, 600))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
