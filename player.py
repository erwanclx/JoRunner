import pygame
from settings import *
import time
import sys

class Player:
    def __init__(self, game):
        self.game = game
        self.x = TILE_WIDTH + SCREEN_OFFSET
        self.y = SCREEN_HEIGHT - TILE_HEIGHT
        self.player_image = pygame.image.load('assets/player.png')

        self.cooldown_time = 0.1
        self.last_move_time = time.time()

        self.images = ['Marin_1.png', 'Marin_2.png', 'Marin_3.png', 'Marin_4.png']
        self.left_image = pygame.image.load('assets/player/Marin_left.png')
        self.left_image_wind = pygame.image.load('assets/player_wind/Wind_Left.png')
        self.right_image = pygame.image.load('assets/player/Marin_right.png')
        self.right_image_wind = pygame.image.load('assets/player_wind/Wind_Right.png')
        # self.images = ['0.png', '1.png', '2.png', '3.png']
        self.sprite_index = 0

        self.cooldown_time = 0.2
        self.last_move_time = time.time()

        self.last_sprite_time = time.time()

        self.target_x = self.x
        self.moving = False


    def movement(self):
        
        # if time.time() - self.last_move_time >= self.cooldown_time:
        #     keys = pygame.key.get_pressed()
        #     if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_q]:
        #         scaled_size = self.calculate_scaled_size()
        #         current_sprite = pygame.image.load('assets/player/Marin_left.png')
        #         self.game.screen.blit(pygame.transform.scale(current_sprite, scaled_size), (self.x, self.y - 100))
        #         self.x -= TILE_WIDTH
        #         self.x = max(0 + SCREEN_OFFSET, self.x)
        #         self.last_move_time = time.time()
        #     if keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_e]:
        #         scaled_size = self.calculate_scaled_size()
        #         current_sprite = pygame.image.load('assets/player/Marin_right.png')
        #         self.game.screen.blit(pygame.transform.scale(current_sprite, scaled_size), (self.x, self.y - 100))
        #         self.x += TILE_WIDTH
        #         self.x = min(SCREEN_WIDTH - TILE_WIDTH + SCREEN_OFFSET , self.x)
        #         self.last_move_time = time.time()
        if not self.moving and time.time() - self.last_move_time >= self.cooldown_time:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_q]:
                self.target_x = max(0 + SCREEN_OFFSET, self.x - TILE_WIDTH)
                self.moving = True
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_e]:
                self.target_x = min(SCREEN_WIDTH - TILE_WIDTH + SCREEN_OFFSET, self.x + TILE_WIDTH)
                self.moving = True

        if self.moving and time.time() - self.last_move_time >= self.cooldown_time:
            self.interpolate_movement()

    def interpolate_movement(self):
        speed = 50
        direction = 1 if self.target_x > self.x else -1

        self.x += speed * direction

        if direction == 1 and self.x >= self.target_x or direction == -1 and self.x <= self.target_x:
            self.x = self.target_x
            self.moving = False

    def get_rect(self):
        colision = pygame.Rect(self.x, self.y, TILE_WIDTH - 150, TILE_HEIGHT)
        colision.x += 75
        return colision
    
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
        # current_sprite = pygame.image.load('assets/player/' + self.images[self.sprite_index])
        if self.moving:
            current_sprite = self.left_image if self.target_x < self.x else self.right_image
            
            self.game.screen.blit(pygame.transform.scale(current_sprite, scaled_size), (self.x, self.y - 100))
            # Add wind
            if self.target_x < self.x:
                self.game.screen.blit(pygame.transform.scale(self.left_image_wind, scaled_size), (self.x, self.y - 100))
            else:
                self.game.screen.blit(pygame.transform.scale(self.right_image_wind, scaled_size), (self.x, self.y - 100))
            # self.game.screen.blit(pygame.transform.scale(self.left_image_wind, scaled_size), (self.x, self.y - 100))
        else:
            current_sprite = pygame.image.load('assets/player/' + self.images[self.sprite_index])
            self.game.screen.blit(pygame.transform.scale(current_sprite, scaled_size), (self.x, self.y - 100))

        if time.time() - self.last_sprite_time >= 0.1:
            self.sprite_index = (self.sprite_index + 1) % len(self.images)
            self.last_sprite_time = time.time()

        # pygame.draw.rect(self.game.screen, (255, 0, 0), self.get_rect(), 2)

    def update(self):
        self.movement()
        self.draw()

    @property
    def position(self):
        return self.x, self.y
    
    @property
    def tile(self):
        return self.game.map.world_map[self.position]