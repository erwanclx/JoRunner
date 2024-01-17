import pygame
from game import Game
from settings import *
import sys
from pyvidplayer2 import Video

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

        self.fade_alpha = 0

        self.background_sound = pygame.mixer.Sound('assets/sounds/Training_Montage.mp3')
        self.background_sound.set_volume(0.1)
        self.background_sound.play(-1)

        self.video = Video('assets/video/intro.mov')

        self.pending_start = True
    

    def draw(self):
        self.fade_alpha += 10
        if self.fade_alpha > 255:
            self.fade_alpha = 255

        self.menu_background.set_alpha(self.fade_alpha)

        self.screen.blit(self.menu_background, (0, 0))

        scaled_play_button = pygame.transform.scale(self.play_button, (self.play_button_width // 2, self.play_button_height // 2))
        scaled_quit_button = pygame.transform.scale(self.quit_button, (self.quit_button_width // 2, self.play_button_height // 2))

        scaled_play_button.set_alpha(self.fade_alpha)
        scaled_quit_button.set_alpha(self.fade_alpha)

        self.screen.blit(scaled_play_button, (self.play_button_x, self.play_button_y))
        self.screen.blit(scaled_quit_button, (self.quit_button_x, self.quit_button_y))

    def draw_banner(self):
        title_font = pygame.font.Font('assets/fonts/pixel.ttf', 50)
        title_text = title_font.render('JoRunner', True, (255, 255, 255))
        title_text_width = pygame.Surface.get_width(title_text)
        title_text_height = pygame.Surface.get_height(title_text)
        self.screen.blit(title_text, ((self.menu_width - title_text_width) // 2, (self.menu_height - title_text_height) // 2 - 100))

        subtitle_font = pygame.font.Font('assets/fonts/pixel.ttf', 20)
        subtitle_text = subtitle_font.render("Appuyez sur espace pour aider Marin à rejoindre les Jeux Olympiques", True, (255, 255, 255))
        subtitle_text_width = pygame.Surface.get_width(subtitle_text)
        subtitle_text_height = pygame.Surface.get_height(subtitle_text)
        self.screen.blit(subtitle_text, ((self.menu_width - subtitle_text_width) // 2, (self.menu_height - subtitle_text_height) // 2 - 50))


    def play(self):
        self.background_sound.stop()
        # video_player = pygame.display.set_mode(self.video.current_size)
        while self.video.active:
            self.video.set_volume(0.1)
            self.video.change_resolution((self.menu_height))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.video.active = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                        self.video.active = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    if self.video.current_size[0] - 50 < mouse_x < self.video.current_size[0] + 50 and 0 < mouse_y < 100:
                        self.video.active = False

            self.screen.fill((0, 0, 0))
            if self.video.draw(self.screen, ((self.menu_width - self.video.current_size[0]) // 2, (self.menu_height - self.video.current_size[1]) // 2), force_draw=False):
                pygame.display.update()

            pygame.time.wait(16)
        self.video.close()
        self.draw_banner()
        pygame.display.flip()

        while self.pending_start:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.pending_start = False
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


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
