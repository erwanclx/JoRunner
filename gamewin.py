import pygame
from settings import *
import sys

class GameWin:
    def __init__(self, game):
        self.game = game
        self.x = 0
        self.y = 0
        self.width = self.game.menu_width
        self.height = self.game.menu_height
        self.image = pygame.image.load('assets/menu/game_win.png')
        self.image = pygame.transform.scale(self.image, (self.game.menu_width, self.game.menu_height))

        # self.game_win_sound = pygame.mixer.Sound('assets/sounds/win/background.mp3')
        # self.game_win_sound.set_volume(0.1)
        # self.game_win_sound.play()

        self.quit_button_image = pygame.image.load('assets/menu/button/quit.png')
        self.quit_button_width = pygame.Surface.get_width(self.quit_button_image)
        self.quit_button_height = pygame.Surface.get_height(self.quit_button_image)
        self.quit_button_x = (self.game.menu_width - self.quit_button_width) // 2
        self.quit_button_y = self.game.menu_height - self.quit_button_height - 50


    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))

        self.game.screen.blit(self.quit_button_image, (self.quit_button_x, self.quit_button_y))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.quit_button_x <= event.pos[0] <= self.quit_button_x + self.quit_button_width and self.quit_button_y <= event.pos[1] <= self.quit_button_y + self.quit_button_height:
                        pygame.quit()
                        sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

