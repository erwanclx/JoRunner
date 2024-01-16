import pygame
from settings import *

class Time:
    def __init__(self, game, level):
        self.game = game
        self.level = level
        # self.level_time = level * LEVEL_TIME
        self.level_time = LEVEL_TIME
        self.timer_start = pygame.time.get_ticks()
        self.remaining_time = self.level_time

    
    def update_timer(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.timer_start
        elapsed_time = int(elapsed_time / 1000)
        self.remaining_time = max(0, self.level_time - elapsed_time)
        self.game.remaining_time = self.remaining_time
        if self.remaining_time == 0:
            self.game.new_game()