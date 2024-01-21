import pygame
from settings import *
import time
from utils import resource_path

class Life:
    def __init__(self, game, life):
        self.game = game
        self.life = life
        self.life_fill = pygame.image.load(resource_path('assets/hearts/heart_fill.png'))
        self.life_empty = pygame.image.load(resource_path('assets/hearts/heart_empty.png'))

        self.pixel_font = pygame.font.Font(resource_path('assets/fonts/pixel.ttf'), 32)

        self.frame = pygame.image.load(resource_path('assets/frame.png'))
        self.frame_width = 1226
        self.frame_height = 558

        self.coins_ui_sprite = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png']
        self.coins_sprite_index = 0

        
        self.cooldown_time = 0.2
        self.last_move_time = time.time()

        self.timer_ui_sprite = ['bar_1.png', 'bar_2.png', 'bar_3.png', 'bar_4.png', 'bar_5.png', 'bar_6.png']
        self.timer_sprite_index = 0

    def set_life(self):
        for i in range(self.life):
            self.game.screen.blit(pygame.transform.scale(self.life_fill, (ICONS_SIZE, ICONS_SIZE)), (SCREEN_WIDTH - 20 + i * 50, 100))
        for i in range(self.life, DEFAULT_LIVES):
            self.game.screen.blit(pygame.transform.scale(self.life_empty, (ICONS_SIZE, ICONS_SIZE)), (SCREEN_WIDTH - 20 + i * 50, 100))

    def set_coin(self):
        coin = pygame.image.load(resource_path('assets/bonus/coin/' + self.coins_ui_sprite[self.coins_sprite_index]))
        self.game.screen.blit(pygame.transform.scale(coin, (ICONS_SIZE, ICONS_SIZE)), (SCREEN_WIDTH - 30 + 2 * 50, 165))
        if time.time() - self.last_move_time >= self.cooldown_time:
            self.coins_sprite_index = (self.coins_sprite_index + 1) % len(self.coins_ui_sprite)
            self.last_move_time = time.time()   

        text = self.pixel_font.render(str(self.game.score), True, (52, 53, 65))
        # text = self.pixel_font.render(str(self.game.score), True, (255, 216, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH - 40 + 2 * 50, 200)
        self.game.screen.blit(text, textRect)    


    def set_time(self):
        # # print(self.game.remaining_time)
        timer_image_path = 'assets/time/' + self.timer_ui_sprite[self.timer_sprite_index]
        timer_image = pygame.image.load(resource_path(timer_image_path))
        scaled_timer_image = pygame.transform.scale(timer_image, (timer_image.get_width() // 3, timer_image.get_height() // 3))

        self.game.screen.blit(scaled_timer_image, (SCREEN_WIDTH - 120 + 1 * 50, 20))

        time_per_sprite = LEVEL_TIME / len(self.timer_ui_sprite)
        elapsed_time = LEVEL_TIME - self.game.remaining_time
        sprite_index = min(int(elapsed_time / time_per_sprite), len(self.timer_ui_sprite) - 1)

        if sprite_index != self.timer_sprite_index:
            self.timer_sprite_index = sprite_index
        
        text = self.pixel_font.render(str(self.game.remaining_time), True, (255, 216, 0))
        textRect = text.get_rect()

        if self.game.remaining_time < 5:
            textRect.center = (SCREEN_WIDTH/2 + SCREEN_OFFSET - 15, SCREEN_HEIGHT/2 - 50)
            text = pygame.transform.scale(text, (text.get_width() * 2, text.get_height() * 2))

            # textRect.center = (SCREEN_WIDTH/2 + SCREEN_OFFSET, 55)
            # textRect.center = (SCREEN_WIDTH/2 - SCREEN_OFFSET, 55)
        else:
            textRect.center = (SCREEN_WIDTH - 150 + 1 * 50, 55)

        self.game.screen.blit(text, textRect)

    def draw(self):
        self.game.screen.blit(pygame.transform.scale(self.frame, (self.frame_width/10, self.frame_height/10)), (SCREEN_WIDTH, 100 + 70))
        self.set_life()
        self.set_coin()
        self.set_time()


    def update(self):
        self.draw()