import pygame
from settings import *

class Life:
    def __init__(self, game, life):
        self.game = game
        self.life = life
        self.life_fill = pygame.image.load('assets/hearts/heart_fill.png')
        self.life_empty = pygame.image.load('assets/hearts/heart_empty.png')

    def draw(self):
        for i in range(self.life):
            # self.game.screen.blit(self.life_fill, (SCREEN_OFFSET + i * 50, 0))
            # Using ICONS_SIZE
            self.game.screen.blit(pygame.transform.scale(self.life_fill, (ICONS_SIZE, ICONS_SIZE)), (SCREEN_OFFSET + i * 50, 0))
        for i in range(self.life, DEFAULT_LIVES):
            # self.game.screen.blit(self.life_empty, (SCREEN_OFFSET + i * 50, 0))
            # Using ICONS_SIZE
            self.game.screen.blit(pygame.transform.scale(self.life_empty, (ICONS_SIZE, ICONS_SIZE)), (SCREEN_OFFSET + i * 50, 0))

    def update(self):
        self.draw()