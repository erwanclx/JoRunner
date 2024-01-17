import pygame
from settings import *
import sys
from pyvidplayer2 import Video


class LevelUp:
    def __init__(self, game, level):
        self.game = game
        self.level = level

        self.screen = self.game.screen

        self.video = Video(f'assets/video/level_{level}.mov')

        self.pending_start = True

    def draw_banner(self):
        title_font = pygame.font.Font('assets/fonts/pixel.ttf', 50)
        title_text = title_font.render('Félicitations !', True, (255, 255, 255))
        title_text_width = pygame.Surface.get_width(title_text)
        title_text_height = pygame.Surface.get_height(title_text)
        self.screen.blit(title_text, ((SCREEN_FULL_WIDTH - title_text_width) // 2, (SCREEN_HEIGHT - title_text_height) // 2 - 100))

        subtitle_font = pygame.font.Font('assets/fonts/pixel.ttf', 20)
        subtitle_text = subtitle_font.render("Appuyez sur espace pour continuer", True, (255, 255, 255))
        subtitle_text_width = pygame.Surface.get_width(subtitle_text)
        subtitle_text_height = pygame.Surface.get_height(subtitle_text)
        self.screen.blit(subtitle_text, ((SCREEN_FULL_WIDTH - subtitle_text_width) // 2, (SCREEN_HEIGHT - subtitle_text_height) // 2 - 50))

    def play(self):
        self.game.level_sound.stop()
        while self.video.active:
            self.video.set_volume(0.1)
            self.video.change_resolution((SCREEN_HEIGHT))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))
            if self.video.draw(self.screen, ((SCREEN_FULL_WIDTH - self.video.current_size[0]) // 2, (SCREEN_HEIGHT - self.video.current_size[1]) // 2), force_draw=False):
                    pygame.display.update()

            pygame.time.wait(16)
        self.video.close()
        self.draw_banner()
        pygame.display.flip()

        self.game.level_sound = pygame.mixer.Sound(f'assets/maps/{self.game.level+1}/music.mp3')
        self.game.level_sound.set_volume(0.1)
        self.game.level_sound.play()

        while self.pending_start:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.pending_start = False
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        self.game.reset_values()
        