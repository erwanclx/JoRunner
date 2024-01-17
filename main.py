import pygame
from game import Game
from settings import *
import sys

class Menu:
    def __init__(self):
        self.game = Game()

        self.menu_width = 1000
        self.menu_height = 516

        pygame.init()
        self.screen = pygame.display.set_mode((self.menu_width, self.menu_height))
        pygame.display.set_caption("JoRunner")

        self.menu_background = pygame.image.load('assets/menu/background.png')

        self.banner = pygame.image.load('assets/menu/banner.png')
        self.banner_width = pygame.Surface.get_width(self.banner)
        self.banner_height = pygame.Surface.get_height(self.banner)

        self.play_button = pygame.image.load('assets/menu/button/play.png')
        self.play_button_width = pygame.Surface.get_width(self.play_button)
        self.play_button_height = pygame.Surface.get_height(self.play_button)

        self.quit_button = pygame.image.load('assets/menu/button/quit.png')
        self.quit_button_width = pygame.Surface.get_width(self.quit_button)
        self.quit_button_height = pygame.Surface.get_height(self.quit_button)

        self.play_button_x = (self.menu_width - self.play_button_width // 2) // 2
        self.play_button_y = (self.menu_height - self.play_button_height // 2) // 2 + 50

        self.quit_button_x = (self.menu_width - self.quit_button_width // 2) // 2
        self.quit_button_y = (self.menu_height + self.play_button_height // 2) // 2 + 75
    

    def draw(self):
        self.screen.blit(self.menu_background, (0, 0))
        
        scaled_play_button = pygame.transform.scale(self.play_button, (self.play_button_width // 2, self.play_button_height // 2))
        scaled_quit_button = pygame.transform.scale(self.quit_button, (self.quit_button_width // 2, self.play_button_height // 2))

        self.screen.blit(scaled_play_button, (self.play_button_x, self.play_button_y))
        self.screen.blit(scaled_quit_button, (self.quit_button_x, self.quit_button_y))

    def play(self):
        pygame.quit()
        self.game = Game()
        self.game.run()

    def quit(self):
        pygame.quit()
        sys.exit()

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    if self.play_button_x < mouse_x < self.play_button_x + self.play_button_width // 2 and self.play_button_y < mouse_y < self.play_button_y + self.play_button_height // 2:
                        self.play()

                    elif self.quit_button_x < mouse_x < self.quit_button_x + self.quit_button_width // 2 and self.quit_button_y < mouse_y < self.quit_button_y + self.quit_button_height // 2:
                        self.quit()

            self.draw()
            pygame.display.flip()

if __name__ == "__main__":
    menu = Menu()
    menu.run()