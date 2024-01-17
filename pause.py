import pygame
from settings import *
import sys

class Pause:
    def __init__(self, game):
        self.game = game

        self.menu_width = SCREEN_OFFSET + SCREEN_WIDTH + SCREEN_OFFSET
        self.menu_height = SCREEN_HEIGHT

        self.pause_play = pygame.image.load('assets/menu/button/play.png')
        self.pause_play_width = pygame.Surface.get_width(self.pause_play)
        self.pause_play_height = pygame.Surface.get_height(self.pause_play)

        self.pause_quit = pygame.image.load('assets/menu/button/quit.png')
        self.pause_quit_width = pygame.Surface.get_width(self.pause_quit)
        self.pause_quit_height = pygame.Surface.get_height(self.pause_quit)

        self.pause_play_x = (self.menu_width - self.pause_play_width // 2) // 2
        self.game.pause_play_x = self.pause_play_x
        self.pause_play_y = (self.menu_height - self.pause_play_height // 2) // 2 + 50
        self.game.pause_play_y = self.pause_play_y

        self.pause_quit_x = (self.menu_width - self.pause_quit_width // 2) // 2
        self.game.pause_quit_x = self.pause_quit_x

        self.pause_quit_y = (self.menu_height + self.pause_play_height // 2) // 2 + 75
        self.game.pause_quit_y = self.pause_quit_y

        self.play_hover = False
        self.quit_hover = False

    def draw(self):
        if self.game.pause == True:

            self.scaled_pause_play = pygame.transform.scale(self.pause_play, (self.pause_play_width // 2, self.pause_play_height // 2))
            self.scaled_pause_quit = pygame.transform.scale(self.pause_quit, (self.pause_quit_width // 2, self.pause_play_height // 2))

            self.game.screen.blit(self.scaled_pause_play, (self.pause_play_x, self.pause_play_y))

            self.game.screen.blit(self.scaled_pause_quit, (self.pause_quit_x, self.pause_quit_y))


            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    if self.pause_play_x < mouse_x < self.pause_play_x + self.pause_play_width // 2 and self.pause_play_y < mouse_y < self.pause_play_y + self.pause_play_height // 2:
                        print("Play")
                        self.play()

                    elif self.pause_quit_x < mouse_x < self.pause_quit_x + self.pause_quit_width // 2 and self.pause_quit_y < mouse_y < self.pause_quit_y + self.pause_quit_height // 2:
                        self.quit()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def play(self):
        self.game.pause = False
        
    def quit(self):
        pygame.quit()
        sys.exit()
