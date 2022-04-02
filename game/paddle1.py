import pygame
from constants import *

class Paddle1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.points = 0