import pygame
from settings import *

class GameOver:
    def __init__(self, game):
        self.game = game
        self.game_over = True
        self.game_over_screen = pygame.image.load("assets/gameover/background.png")

        self.game_over_sound = pygame.mixer.Sound('assets/gameover/gameover_sound.mp3')
        self.game_over_sound.play()
        self.game_over_sound.set_volume(0.5)
        
        self.game_over_screen_width = self.game_over_screen.get_width()
        self.game_over_screen_height = self.game_over_screen.get_height()

        self.game_over_screen_rect = self.game_over_screen.get_rect()
        self.game_over_screen_rect.center = (SCREEN_WIDTH/2 + SCREEN_OFFSET, SCREEN_HEIGHT/2)

        self.game_over_surface = pygame.Surface((self.game_over_screen_width, self.game_over_screen_height))
        self.game_over_surface.blit(self.game_over_screen, (0, 0))
        self.game_over_alpha = 0

        self.fade_surface = pygame.Surface((SCREEN_WIDTH + SCREEN_OFFSET + SCREEN_OFFSET, SCREEN_HEIGHT))
        self.fade_surface.fill((0, 0, 0))
        self.fade_alpha = 0

        self.game_over_button = pygame.image.load("assets/gameover/replay.png")
        self.game_over_button_width = pygame.Surface.get_width(self.game_over_button)
        self.game_over_button_height = pygame.Surface.get_height(self.game_over_button)

        self.game_over_button_x = (SCREEN_WIDTH + SCREEN_OFFSET + SCREEN_OFFSET - self.game_over_button_width // 2) // 2
        self.game_over_button_y = (SCREEN_HEIGHT - self.game_over_button_height // 2) // 2 + 200

        self.game_over_button = pygame.transform.scale(self.game_over_button, (self.game_over_button_width // 2, self.game_over_button_height // 2))
    
    def replay(self):
        self.game.reset_level()
        self.game.new_game()
        self.game_over = False
        self.game.game_over = False
        self.fade_alpha = 0

    def draw(self):        
        self.fade_alpha += 5 
        self.fade_surface.set_alpha(self.fade_alpha)
        self.game.screen.blit(self.fade_surface, (0, 0))

        self.game_over_alpha += 5 
        self.game_over_surface.set_alpha(self.game_over_alpha)
        self.game.screen.blit(self.game_over_surface, self.game_over_screen_rect)

        if self.fade_alpha >= 255:
            self.game.screen.blit(self.game_over_button, (self.game_over_button_x, self.game_over_button_y))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    if self.game_over_button_x < mouse_x < self.game_over_button_x + self.game_over_button_width // 2 and self.game_over_button_y < mouse_y < self.game_over_button_y + self.game_over_button_height // 2:
                        print("Replay")
                        self.replay()

        pygame.display.flip()