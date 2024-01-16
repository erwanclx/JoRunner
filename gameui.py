import pygame
from settings import *
import time

class Life:
    def __init__(self, game, life):
        self.game = game
        self.life = life
        self.life_fill = pygame.image.load('assets/hearts/heart_fill.png')
        self.life_empty = pygame.image.load('assets/hearts/heart_empty.png')

        self.frame = pygame.image.load('assets/frame.png')
        self.frame_width = 1226
        self.frame_height = 558

        self.coins_ui_sprite = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png']
        self.coins_sprite_index = 0

        self.cooldown_time = 0.2
        self.last_move_time = time.time()

    def draw(self):

        self.game.screen.blit(pygame.transform.scale(self.frame, (self.frame_width/10, self.frame_height/10)), (SCREEN_WIDTH, 100 + 70))

        for i in range(self.life):
            # self.game.screen.blit(self.life_fill, (SCREEN_OFFSET + i * 50, 0))
            # Using ICONS_SIZE
            self.game.screen.blit(pygame.transform.scale(self.life_fill, (ICONS_SIZE, ICONS_SIZE)), (SCREEN_WIDTH - 20 + i * 50, 100))
        for i in range(self.life, DEFAULT_LIVES):
            # self.game.screen.blit(self.life_empty, (SCREEN_OFFSET + i * 50, 0))
            # Using ICONS_SIZE
            self.game.screen.blit(pygame.transform.scale(self.life_empty, (ICONS_SIZE, ICONS_SIZE)), (SCREEN_WIDTH - 20 + i * 50, 100))


        coin = pygame.image.load('assets/bonus/coin/' + self.coins_ui_sprite[self.coins_sprite_index])

        # Using ICONS_SIZE
        self.game.screen.blit(pygame.transform.scale(coin, (ICONS_SIZE, ICONS_SIZE)), (SCREEN_WIDTH - 30 + i * 50, 165))
        if time.time() - self.last_move_time >= self.cooldown_time:
            self.coins_sprite_index = (self.coins_sprite_index + 1) % len(self.coins_ui_sprite)
            self.last_move_time = time.time()

        # Add score text
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(self.game.score), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH - 30 + i * 50, 200)
        self.game.screen.blit(text, textRect)





    def update(self):
        self.draw()