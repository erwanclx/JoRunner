from settings import *
from map import *
from gameui import Life
import pygame

class Collectibles:
    def __init__(self, game, x, y):
        self.game = game
        self.mini_map = mini_map
        self.size = (TILE_WIDTH, TILE_HEIGHT)
        self.x = SCREEN_OFFSET/2 + x * TILE_WIDTH
        self.y = y * TILE_HEIGHT + int(SCREEN_HEIGHT/4)
        self.speed = 5

        # self.collectible_type_weights = (0, 0, 1)
        self.collectible_type_weights = (0.88, 0.07, 0.05)
        self.collectible_type_array = ['coin', 'heart', 'bonus_jo']
        self.collectible_type = random.choices(self.collectible_type_array, weights=self.collectible_type_weights)[0]
        
        self.images = {
            'coin': pygame.image.load('assets/bonus/coin.png'),
            'heart': pygame.image.load('assets/bonus/wine.png'),
            'bonus_jo': pygame.image.load(f'assets/jo_circle/item/{min(self.game.jo_counter + 1, 5)}.png')
        }

    def get_rect(self):
        # return pygame.Rect(self.x, self.y, TILE_WIDTH + SCREEN_OFFSET, TILE_HEIGHT)
        colision = pygame.Rect(self.x, self.y, TILE_WIDTH - 150, TILE_HEIGHT)
        colision.x += 75
        return colision
    
    def disablejo(self):
        self.collectible_type_weights = (0.88, 0.12)
        self.collectible_type_array = ['coin', 'heart']
        self.collectible_type = random.choices(self.collectible_type_array, weights=self.collectible_type_weights)[0]
        self.images = {
            'coin': pygame.image.load('assets/bonus/coin.png'),
            'heart': pygame.image.load('assets/bonus/wine.png')
        }

    def draw(self):

        img = self.images[self.collectible_type]
        img_rect = img.get_rect()
        
        if self.x == 535.3333333333334 + SCREEN_OFFSET/2:
            perspective_factor = 0.4 
        elif self.x == 0.0 + SCREEN_OFFSET/2:
            perspective_factor = -0.4
        else:
            perspective_factor = 0.2

        x_offset = (self.y / SCREEN_HEIGHT) * (SCREEN_WIDTH / 2) * perspective_factor
        adjusted_x = self.x + x_offset

        if self.x == 535.3333333333334 + SCREEN_OFFSET/2:
            img_rect.topright = (adjusted_x + TILE_WIDTH + SCREEN_OFFSET / 2 - SCREEN_OFFSET - 100, self.y + TILE_HEIGHT / 2)
        elif self.x == 0.0 + SCREEN_OFFSET/2:
            img_rect.topleft = (adjusted_x + TILE_WIDTH + SCREEN_OFFSET / 2, self.y + TILE_HEIGHT / 2)  # Adjusted for top right
        else:
            tile_rect = pygame.Rect(self.x, self.y, TILE_WIDTH + SCREEN_OFFSET, TILE_HEIGHT)
            img_rect.center = tile_rect.center

        shadow_radius = 40 // 2  
        shadow_radius_x = TILE_WIDTH // 10  # Rayon horizontal de l'ombre
        shadow_radius_y = TILE_HEIGHT // 20
        shadow_color = (0, 0, 0, 50)
        shadow_surface = pygame.Surface((shadow_radius_x * 2, shadow_radius_y * 2), pygame.SRCALPHA)

        shadow_center = (img_rect.centerx, img_rect.centery + 25 + shadow_radius)
        pygame.draw.ellipse(shadow_surface, shadow_color, (0, 0, shadow_radius_x * 2, shadow_radius_y * 2))
        self.game.screen.blit(shadow_surface, (shadow_center[0] - shadow_radius_x, shadow_center[1] - shadow_radius_y))

        # Dessine l'image sur l'écran
        self.game.screen.blit(img, img_rect.topleft)

        # pygame.draw.rect(self.game.screen, (255, 0, 0), self.get_rect(), 2)




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
                if self.game.score == SCORE_TO_CHANGE_LEVEL:
                    self.game.level += 1

                    if self.game.level == 4:
                        print("You win!")
                        self.game.reset_values()
                    else:
                        self.game.new_game()
                    print("Level: ", self.game.level)
                    
            elif self.collectible_type == 'heart':
                self.game.lives += 1
                self.game.lives = min(self.game.lives, 3)
                self.game.life = Life(self.game, self.game.lives)
                print("Lives: ", self.game.lives)
            elif self.collectible_type == 'bonus_jo':
                self.game.jo_counter += 1
                self.game.jo_counter = min(self.game.jo_counter, 5)
                print("Jo Counter: ", self.game.jo_counter)
                if self.game.jo_counter == 5:
                    self.disablejo()
                    print("Bonus Jo disabled")