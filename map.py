import pygame
import random
from settings import *
from rich import print

_ = False
mini_map = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, col in enumerate(row):
                if col:
                    self.world_map[(i, j)] = col

    def draw(self):
        # [pygame.draw.rect(self.game.screen, ((255, 255, 255, 128)), (pos[0] * TILE_WIDTH + SCREEN_OFFSET, pos[1] * TILE_HEIGHT + int(SCREEN_HEIGHT/3), TILE_WIDTH, TILE_HEIGHT), 2)
        # for pos in self.world_map]
        # Same with shadow surface
        
        # Draw each line of the map
        for j, row in enumerate(self.mini_map):
            for i, col in enumerate(row):
                if col:
                    pygame.draw.rect(self.game.screen, ((67, 64, 64)), (i * TILE_WIDTH + SCREEN_OFFSET, j * TILE_HEIGHT + int(SCREEN_HEIGHT/3), TILE_WIDTH, 1), 2)

        pass