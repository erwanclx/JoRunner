import pygame
import subprocess
import webbrowser
from game import Game
from settings import *
import sys
from pyvidplayer2 import Video
from utils import resource_path

class Menu:
    def __init__(self):
        
        self.game = Game()

        self.menu_width = 1000
        self.menu_height = 516

        pygame.init()
        # self.screen = pygame.display.set_mode((self.menu_width, self.menu_height))
        # pygame.display.set_caption("JoRunner")
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("JoRunner")
        self.menu_width, self.menu_height = pygame.display.get_surface().get_size()
        self.scale_factor = self.screen.get_height() / (SCREEN_HEIGHT)


        # self.menu_background = pygame.image.load('assets/menu/background.png')
        self.menu_background = pygame.image.load(resource_path('assets/menu/background.png'))
        

        # self.banner = pygame.image.load('assets/menu/banner.png')
        self.banner = pygame.image.load(resource_path('assets/menu/banner.png'))
        self.banner_width = pygame.Surface.get_width(self.banner)
        self.banner_height = pygame.Surface.get_height(self.banner)

        # self.play_button = pygame.image.load('assets/menu/button/play.png')
        self.play_button = pygame.image.load(resource_path('assets/menu/button/play.png'))
        self.play_button_width = pygame.Surface.get_width(self.play_button)
        self.play_button_height = pygame.Surface.get_height(self.play_button)

        # self.quit_button = pygame.image.load('assets/menu/button/quit.png')
        self.quit_button = pygame.image.load(resource_path('assets/menu/button/quit.png'))
        self.quit_button_width = pygame.Surface.get_width(self.quit_button)
        self.quit_button_height = pygame.Surface.get_height(self.quit_button)

        self.play_button_x = (self.menu_width - self.play_button_width // 2) // 2
        self.play_button_y = (self.menu_height - self.play_button_height // 2) // 2 + 50

        self.quit_button_x = (self.menu_width - self.quit_button_width // 2) // 2
        self.quit_button_y = (self.menu_height + self.play_button_height // 2) // 2 + 75

        self.fade_alpha = 0

        # self.background_sound = pygame.mixer.Sound('assets/sounds/Training_Montage.mp3')
        self.background_sound = pygame.mixer.Sound(resource_path('assets/sounds/Training_Montage.mp3'))
        self.background_sound.set_volume(0.1)
        self.background_sound.play(-1)

        # self.video = Video('assets/video/intro.mov')
        self.video = Video(resource_path('assets/video/intro.mov'))

        self.pending_start = True
    

    def draw(self):
        self.fade_alpha += 10
        if self.fade_alpha > 255:
            self.fade_alpha = 255

        aspect_ratio = self.menu_background.get_width() / self.menu_background.get_height()
        new_width = int(self.menu_height * aspect_ratio)
        new_height = self.menu_height

        scaled_background = pygame.transform.scale(self.menu_background, (new_width, new_height))
        scaled_background.set_alpha(self.fade_alpha)

        x_offset = (self.menu_width - new_width) // 2
        y_offset = (self.menu_height - new_height) // 2

        self.screen.blit(scaled_background, (x_offset, y_offset))

        self.menu_background.set_alpha(self.fade_alpha)

        scaled_play_button = pygame.transform.scale(self.play_button, (self.play_button_width // 2, self.play_button_height // 2))
        scaled_quit_button = pygame.transform.scale(self.quit_button, (self.quit_button_width // 2, self.play_button_height // 2))

        scaled_play_button.set_alpha(self.fade_alpha)
        scaled_quit_button.set_alpha(self.fade_alpha)

        self.screen.blit(scaled_play_button, (self.play_button_x, self.play_button_y))
        self.screen.blit(scaled_quit_button, (self.quit_button_x, self.quit_button_y))

        
        try:
            subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except:
            error_font = pygame.font.Font(resource_path('assets/fonts/pixel.ttf'), 30)
            error_text = error_font.render("FFmpeg n'est pas installé sur votre système. Veuillez l'installer pour exécuter ce jeu.", True, (255, 0, 0))
            error_text_width = pygame.Surface.get_width(error_text)
            error_text_height = pygame.Surface.get_height(error_text)
            
            banner_rect = pygame.Rect((self.menu_width - error_text_width - 20) // 2, (self.menu_height - error_text_height - 210), error_text_width + 20, error_text_height + 20)
            pygame.draw.rect(self.screen, (255, 255, 255), banner_rect)
            
            self.screen.blit(error_text, ((self.menu_width - error_text_width) // 2, (self.menu_height - error_text_height - 200)))

            button_rect = pygame.Rect((self.menu_width - 300) // 2, (self.menu_height - error_text_height - 115), 300, 50)
            pygame.draw.rect(self.screen, (223, 69, 15), button_rect)
            
            button_font = pygame.font.Font(resource_path('assets/fonts/pixel.ttf'), 20)
            button_text = button_font.render("Comment installer ?", True, (255, 255, 255))
            button_text_width = pygame.Surface.get_width(button_text)
            self.screen.blit(button_text, ((self.menu_width - button_text_width) // 2, (self.menu_height - error_text_height - 100)))

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0]:
                    webbrowser.open("https://github.com/erwanclx/JoRunner")
                    sys.exit()

    def draw_banner(self):
        # title_font = pygame.font.Font('assets/fonts/pixel.ttf', 50)
        title_font = pygame.font.Font(resource_path('assets/fonts/pixel.ttf'), 50)
        title_text = title_font.render('JoRunner', True, (255, 255, 255))
        title_text_width = pygame.Surface.get_width(title_text)
        title_text_height = pygame.Surface.get_height(title_text)
        self.screen.blit(title_text, ((self.menu_width - title_text_width) // 2, (self.menu_height - title_text_height) // 2 - 100))

        # subtitle_font = pygame.font.Font('assets/fonts/pixel.ttf', 20)
        subtitle_font = pygame.font.Font(resource_path('assets/fonts/pixel.ttf'), 20)
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
