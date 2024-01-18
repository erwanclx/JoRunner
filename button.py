import pygame
from settings import *

class Button:
    def __init__(self, game, orientation):
        self.game = game
        self.orientation = orientation
        self.image = pygame.image.load(f'assets/arrows/{orientation}.png')
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_OFFSET + SCREEN_WIDTH + SCREEN_OFFSET - self.rect.width - 10
        self.rect.y = 10

    def update(self):
        self.game.screen.blit(self.image, self.rect)