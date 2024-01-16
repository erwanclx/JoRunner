import pygame
from settings import *
import time
import sys

class Player:
    def __init__(self, game):
        self.game = game
        self.x = TILE_WIDTH
        self.y = SCREEN_HEIGHT - TILE_HEIGHT
        self.player_image = pygame.image.load('assets/player.png')

        self.cooldown_time = 0.1
        self.last_move_time = time.time()

        self.images = ['0.png', '1.png', '2.png', '3.png']
        self.sprite_index = 0

        self.cooldown_time = 0.2
        self.last_move_time = time.time()

        self.last_sprite_time = time.time()


    def movement(self):
        
        if time.time() - self.last_move_time >= self.cooldown_time:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_q]:
                self.x -= TILE_WIDTH
                self.x = max(0, self.x)
                self.last_move_time = time.time()
            if keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_e]:
                self.x += TILE_WIDTH
                self.x = min(SCREEN_WIDTH - TILE_WIDTH, self.x)
                self.last_move_time = time.time()

    def get_rect(self):
        return pygame.Rect(self.x, self.y, TILE_WIDTH, TILE_HEIGHT)
    
    def calculate_scaled_size(self):
        # Calculer la taille adaptée sans déformation
        aspect_ratio = self.player_image.get_width() / self.player_image.get_height()
        new_width = TILE_WIDTH
        new_height = int(TILE_WIDTH / aspect_ratio)
        return new_width, new_height

    def draw(self):
        # scaled_size = self.calculate_scaled_size()
        # self.game.screen.blit(pygame.transform.scale(self.player_image, scaled_size), (self.x, self.y - 100))
        scaled_size = self.calculate_scaled_size()
        current_sprite = pygame.image.load('assets/player/' + self.images[self.sprite_index])
        self.game.screen.blit(pygame.transform.scale(current_sprite, scaled_size), (self.x, self.y - 100))
        if time.time() - self.last_sprite_time >= 0.1:
            self.sprite_index = (self.sprite_index + 1) % len(self.images)
            self.last_sprite_time = time.time()

    def update(self):
        self.movement()
        self.draw()

    @property
    def position(self):
        return self.x, self.y
    
    @property
    def tile(self):
        return self.game.map.world_map[self.position]