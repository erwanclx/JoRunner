from settings import *
from map import *
import pygame

class Collectibles:
    def __init__(self, game, x, y):
        self.game = game
        self.mini_map = mini_map
        self.size = (TILE_WIDTH, TILE_HEIGHT)
        self.x = x * TILE_WIDTH
        self.y = y * TILE_HEIGHT + int(SCREEN_HEIGHT/3)
        self.speed = 2
        self.collectible_type = random.choice(['coin', 'heart'])
        self.images = {
            'coin': pygame.image.load('assets/bonus/coin.png'),
            'heart': pygame.image.load('assets/bonus/wine.png')
        }

    def get_rect(self):
        return pygame.Rect(self.x, self.y, TILE_WIDTH, TILE_HEIGHT)

    def draw(self):
        img = self.images[self.collectible_type]
        img_rect = img.get_rect()

        if self.x == 535.3333333333334:
            perspective_factor = 0.2
        elif self.x == 0.0:
            perspective_factor = -0.2  # Reverse the effect for self.x == 0.0
        else:
            perspective_factor = 0.2

        x_offset = (self.y / SCREEN_HEIGHT) * (SCREEN_WIDTH / 2) * perspective_factor
        adjusted_x = self.x + x_offset

        if self.x == 535.3333333333334:
            img_rect.topright = (adjusted_x + TILE_WIDTH / 2 - 50, self.y + TILE_HEIGHT / 2)
        elif self.x == 0.0:
            img_rect.topleft = (adjusted_x + TILE_WIDTH / 2 + 50, self.y + TILE_HEIGHT / 2)  # Adjusted for top right
        else:
            tile_rect = pygame.Rect(self.x, self.y, TILE_WIDTH, TILE_HEIGHT)
            img_rect.center = tile_rect.center

        self.game.screen.blit(img, img_rect.topleft)





    def update(self):
        self.y += self.speed
        self.draw()

        for collectible in self.game.collectibles:
            if collectible.y > SCREEN_HEIGHT:
                self.game.collectibles.remove(collectible)

        player_rect = self.game.player.get_rect()
        if player_rect.colliderect(self.get_rect()):
            print("Collision between Player and Collectible")
            self.game.collectibles.remove(self)
            if self.collectible_type == 'coin':
                self.game.score += 1
                print("Score: ", self.game.score)
            elif self.collectible_type == 'heart':
                self.game.lives += 1
                self.game.lives = min(self.game.lives, 3)
                print("Lives: ", self.game.lives)