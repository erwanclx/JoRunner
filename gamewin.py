import pygame
from settings import *

class GameWin:
    def __init__(self, game):
        self.game = game
        self.x = 0
        self.y = 0
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.image = pygame.image.load('assets/menu/game_win.png')
        self.image = pygame.transform.scale(self.image, (SCREEN_FULL_WIDTH, SCREEN_HEIGHT))

        self.game_win_sound = pygame.mixer.Sound('assets/sounds/win/background.mp3')
        self.game_win_sound.set_volume(0.1)
        self.game_win_sound.play()

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))