from settings import *
from map import *
from gameui import Life
import pygame
import time
from player import Player

class Obstacle():
    def __init__(self, game, x, y):
        self.game = game
        self.mini_map = mini_map
        self.size = (TILE_WIDTH, TILE_HEIGHT)
        self.x = SCREEN_OFFSET + x * TILE_WIDTH
        self.y = SCREEN_HEIGHT - TILE_HEIGHT * 4
        
        self.speed = 5

        self.frame_count = 0

        # self.images = ['1.png', '2.png', '3.png', '4.png']
        # self.images = ['scooter.png']
        # self.images = ['/hidalgo/0.png', '/hidalgo/1.png', '/hidalgo/2.png', '/hidalgo/3.png']

        self.images = {
            'scooter': ['scooter.png', 'scooter.png', 'scooter.png', 'scooter.png'],
            'hidalgo': ['/hidalgo/0.png', '/hidalgo/1.png', '/hidalgo/2.png', '/hidalgo/3.png'],
            'rat': ['1.png', '2.png', '3.png', '4.png']
        }
        self.choices = ['scooter', 'hidalgo', 'rat']
        self.random_choice = random.choice(self.choices)

        self.sprite_index = 0

        self.cooldown_time = 0.2
        self.last_move_time = time.time()

    def draw(self):

        # img = pygame.image.load('assets/rat/' + self.images[self.sprite_index])
        img = pygame.image.load('assets/rat/' + self.images[self.random_choice][self.sprite_index])
        img = pygame.transform.scale(img, (int(img.get_width() * 1.3), int(img.get_height() * 1.3)))

        img_rect = img.get_rect()

        # if self.x == 535.3333333333334 + SCREEN_OFFSET:
        if self.x == 1173.3333333333335 :
            perspective_factor = 0.4 
        elif self.x == 0.0 + SCREEN_OFFSET:
            perspective_factor = -0.4
        else:
            perspective_factor = 0.2

        x_offset = (self.y / SCREEN_HEIGHT) * (SCREEN_WIDTH / 2) * perspective_factor
        adjusted_x = self.x + x_offset

        # if self.x == 535.3333333333334 + SCREEN_OFFSET:
        if self.x == 1173.3333333333335 :
            img_rect.topright = (adjusted_x + TILE_WIDTH / 2 - 125 * ASSETS_MULTIPLIER, self.y)
        elif self.x == 0.0 + SCREEN_OFFSET:
            img_rect.topleft = (adjusted_x + TILE_WIDTH / 2 + 125 * ASSETS_MULTIPLIER, self.y)
        else:
            tile_rect = pygame.Rect(self.x - SCREEN_OFFSET/2, self.y, TILE_WIDTH + SCREEN_OFFSET, TILE_HEIGHT)
            img_rect.center = tile_rect.center
 
        
        
        # pygame.draw.rect(self.game.screen, (255, 0, 0), self.get_rect(), 2)



        self.game.screen.blit(img, img_rect.topleft)
        if time.time() - self.last_move_time >= self.cooldown_time:
            self.sprite_index = (self.sprite_index + 1) % len(self.images)
            self.last_move_time = time.time()

        print("Obstacle position: ", self.x, self.y)

    def get_rect(self):
        colision = pygame.Rect(self.x, self.y, TILE_WIDTH - 175, TILE_HEIGHT)
        colision.x += 75
        return colision

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
            self.game.lives -= 1
            self.game.life = Life(self.game, self.game.lives)
            self.game.player_hit_sound.set_volume(0.5)
            self.game.player_hit_sound.play()

            self.game.player_hurt_time = time.time()
            self.game.player_hurt = True