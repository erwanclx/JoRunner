from settings import *
from map import *
import pygame
import time

class Obstacle():
    def __init__(self, game, x, y):
        self.game = game
        self.mini_map = mini_map
        self.size = (TILE_WIDTH, TILE_HEIGHT)
        self.x = x * TILE_WIDTH
        self.y = SCREEN_HEIGHT - TILE_HEIGHT * 3
        
        self.speed = 2

        self.frame_count = 0

        self.images = ['1.png', '2.png', '3.png', '4.png']
        self.sprite_index = 0

        self.cooldown_time = 0.2
        self.last_move_time = time.time()

    def draw(self):

        img = pygame.image.load('assets/rat/' + self.images[self.sprite_index])
        img_rect = img.get_rect()

        if self.x == 535.3333333333334:
            perspective_factor = 0.2
        elif self.x == 0.0:
            perspective_factor = -0.2
        else:
            perspective_factor = 0.2

        x_offset = (self.y / SCREEN_HEIGHT) * (SCREEN_WIDTH / 2) * perspective_factor
        adjusted_x = self.x + x_offset

        if self.x == 535.3333333333334:
            img_rect.topright = (adjusted_x + TILE_WIDTH / 2 - 50, self.y + TILE_HEIGHT / 2)
        elif self.x == 0.0:
            img_rect.topleft = (adjusted_x + TILE_WIDTH / 2 + 50, self.y + TILE_HEIGHT / 2)
        else:
            tile_rect = pygame.Rect(self.x, self.y, TILE_WIDTH, TILE_HEIGHT)
            img_rect.center = tile_rect.center
        
        self.game.screen.blit(img, img_rect.topleft)
        if time.time() - self.last_move_time >= self.cooldown_time:
            self.sprite_index = (self.sprite_index + 1) % len(self.images)
            self.last_move_time = time.time()

    def get_rect(self):
        return pygame.Rect(self.x, self.y, TILE_WIDTH, TILE_HEIGHT)

    def update(self):
        # self.draw()
        self.y += self.speed
        self.draw()

        for obstacle in self.game.obstacles:
            if obstacle.y > SCREEN_HEIGHT:
                self.game.obstacles.remove(obstacle)

        # Check collision between Obstacle and Obstacle
        for obstacle in self.game.obstacles:
            if obstacle != self:
                if obstacle.get_rect().colliderect(self.get_rect()):
                    print("Collision between Obstacle and Obstacle")
                    self.game.obstacles.remove(obstacle)
        

        player_rect = self.game.player.get_rect()
        if player_rect.colliderect(self.get_rect()):
            print("Collision between Player and Obstacle")
            self.game.obstacles.remove(self)
