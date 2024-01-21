import pygame
from settings import *
import time
import sys
from utils import resource_path

class Player:
    def __init__(self, game):
        self.game = game
        self.x = TILE_WIDTH + SCREEN_OFFSET
        self.y = SCREEN_HEIGHT - TILE_HEIGHT
        self.player_image = pygame.image.load(resource_path('assets/player.png'))

        self.cooldown_time = 0.1
        self.last_move_time = time.time()

        self.hurt_image = pygame.image.load(resource_path('assets/player/hurt.png'))

        self.images = ['1.png', '2.png', '3.png', '4.png']
        self.left_image = pygame.image.load(resource_path(f'assets/player/{self.game.level}/left.png'))
        # self.left_image = pygame.image.load(f'assets/player/{self.game.level}/left.png')
        self.right_image = pygame.image.load(resource_path(f'assets/player/{self.game.level}/right.png'))
        # self.right_image = pygame.image.load(f'assets/player/{self.game.level}/right.png')

        self.left_image_wind = pygame.image.load(resource_path('assets/player_wind/Wind_Left.png'))
        self.right_image_wind = pygame.image.load(resource_path('assets/player_wind/Wind_Right.png'))

        self.sprite_index = 0

        self.cooldown_time = 0.2
        self.last_move_time = time.time()

        self.last_sprite_time = time.time()

        self.player_hurt_time = time.time()

        self.target_x = self.x
        self.moving = False


    def movement(self):
        if not self.moving and time.time() - self.last_move_time >= self.cooldown_time:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_q]:
                self.target_x = max(SCREEN_OFFSET + 50, self.x - TILE_WIDTH + 50)
                # self.target_x = max(0 + SCREEN_OFFSET, self.x - TILE_WIDTH)
                self.moving = True
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_e]:
                # self.target_x = min(SCREEN_WIDTH - TILE_WIDTH + SCREEN_OFFSET, self.x + TILE_WIDTH)
                self.target_x = min(SCREEN_WIDTH - TILE_WIDTH + SCREEN_OFFSET - 50, self.x + TILE_WIDTH - 50)
                self.moving = True

        if self.moving and time.time() - self.last_move_time >= self.cooldown_time:
            self.interpolate_movement()

        # self.target_x = max(0 + SCREEN_OFFSET + 50, min(SCREEN_FULL_WIDTH - SCREEN_OFFSET - 50, self.target_x))

    def interpolate_movement(self):
        speed = 50
        direction = 1 if self.target_x > self.x else -1

        self.x += speed * direction

        if direction == 1 and self.x >= self.target_x or direction == -1 and self.x <= self.target_x:
            self.x = self.target_x
            self.moving = False

    def get_rect(self):
        colision = pygame.Rect(self.x, self.y, TILE_WIDTH - 150, TILE_HEIGHT - 90)
        colision.x += 75
        colision.y += 50
        return colision
    
    def calculate_scaled_size(self):
        aspect_ratio = self.player_image.get_width() / self.player_image.get_height()
        new_width = TILE_WIDTH
        new_height = int(TILE_WIDTH / aspect_ratio)
        return new_width, new_height

    def draw(self):
        scaled_size = self.calculate_scaled_size()
        if self.moving:
            current_sprite = self.left_image if self.target_x < self.x else self.right_image
            
            self.game.screen.blit(pygame.transform.scale(current_sprite, scaled_size), (self.x, self.y - 100))
            if self.target_x < self.x:
                self.game.screen.blit(pygame.transform.scale(self.left_image_wind, scaled_size), (self.x, self.y - 100))
            else:
                self.game.screen.blit(pygame.transform.scale(self.right_image_wind, scaled_size), (self.x, self.y - 100))
        else:
            
            current_sprite = pygame.image.load(resource_path(f'assets/player/{min(self.game.level, LEVEL_NUMBER)}/' + self.images[self.sprite_index]))
            if self.game.player_hurt:
                current_sprite = pygame.image.load(resource_path('assets/player/hurt.png'))
                if time.time() - self.game.player_hurt_time >= 0.5:
                    self.game.player_hurt = False
                    self.game.player_hurt_time = time.time()

            if self.x == 160:
                self.game.screen.blit(pygame.transform.scale(current_sprite, scaled_size), (self.x + 50, self.y - 100))
            elif self.x == 695.3333333333333:
                self.game.screen.blit(pygame.transform.scale(current_sprite, scaled_size), (self.x - 50, self.y - 100))
            else:
                self.game.screen.blit(pygame.transform.scale(current_sprite, scaled_size), (self.x, self.y - 100))

        if time.time() - self.last_sprite_time >= 0.1:
            self.sprite_index = (self.sprite_index + 1) % len(self.images)
            self.last_sprite_time = time.time()

        if DEBUG:
            pygame.draw.rect(self.game.screen, (255, 0, 0), self.get_rect(), 2)

    def update(self):
        self.movement()
        self.draw()

    @property
    def position(self):
        return self.x, self.y
    
    @property
    def tile(self):
        return self.game.map.world_map[self.position]