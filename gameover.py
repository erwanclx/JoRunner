import pygame
from scale import ScaledContent
from settings import *
from utils import resource_path

class GameOver:
    def __init__(self, game):
        self.game = game
        self.game_over = True
        self.game_over_screen = pygame.image.load(resource_path("assets/gameover/background.png"))

        self.scaledBg = ScaledContent(self.game, self.game_over_screen)
        
        self.game_over_back_width, self.game_over_back_height = self.scaledBg.new_width, self.scaledBg.new_height

        self.game_over_screen = pygame.transform.scale(self.game_over_screen, (self.game_over_back_width, self.game_over_back_height))

        self.game_over_sound = pygame.mixer.Sound(resource_path('assets/gameover/gameover_sound.mp3'))
        self.game_over_sound.play()
        self.game_over_sound.set_volume(0.5)

        self.game_over_screen_width = self.game.screen.get_width()
        self.game_over_screen_height = self.game.screen.get_height()


        self.game_over_screen_rect = self.game_over_screen.get_rect()

        self.game_over_surface = pygame.Surface((self.game.menu_width, self.game.menu_height))
        self.game_over_surface.blit(self.game_over_screen, (0, 0))
        self.game_over_alpha = 0

        self.fade_surface = pygame.Surface((self.game.menu_width, self.game.menu_height))
        self.fade_surface.fill((0, 0, 0))
        self.fade_alpha = 0

        self.game_over_button = pygame.image.load(resource_path("assets/gameover/replay.png"))
        self.game_over_button_width = pygame.Surface.get_width(self.game_over_button)
        self.game_over_button_height = pygame.Surface.get_height(self.game_over_button)

        self.game_over_button_x = (self.game.menu_width - self.game_over_button_width // 2) // 2
        self.game_over_button_y = (self.game.menu_height - self.game_over_button_height // 2) // 2 + 200

        self.game_over_button = pygame.transform.scale(self.game_over_button, (self.game_over_button_width // 2, self.game_over_button_height // 2))
    
    def replay(self):
        self.game.reset_level()
        self.game.new_game()
        self.game_over = False
        self.game.game_over = False
        self.fade_alpha = 0

    def draw(self):        

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    if self.game_over_button_x < mouse_x < self.game_over_button_x + self.game_over_button_width // 2 and self.game_over_button_y < mouse_y < self.game_over_button_y + self.game_over_button_height // 2:
                        # print("Replay")
                        self.replay()

        self.fade_alpha += 5 
        self.fade_surface.set_alpha(self.fade_alpha)
        self.game.screen.blit(self.fade_surface, (0, 0))

        self.game_over_alpha += 5 
        self.game_over_surface.set_alpha(self.game_over_alpha)
        self.game.screen.blit(self.game_over_surface, self.game_over_screen_rect)

        if self.fade_alpha >= 255:
            self.game.screen.blit(self.game_over_button, (self.game_over_button_x, self.game_over_button_y))

        pygame.display.flip()