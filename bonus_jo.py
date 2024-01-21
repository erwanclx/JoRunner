import pygame
from settings import *

class BonusJo:
    def __init__(self, game):
        self.game = game

        self.jo_items = ['assets/jo_circle/1.png', 'assets/jo_circle/2.png', 'assets/jo_circle/3.png', 'assets/jo_circle/4.png', 'assets/jo_circle/5.png']
        self.jo_counters = ['assets/jo_circle/empty.png','assets/jo_circle/1.png', 'assets/jo_circle/2.png', 'assets/jo_circle/3.png', 'assets/jo_circle/4.png', 'assets/jo_circle/full.png']

    def scale(self, img):
        return pygame.transform.scale(img, (int(img.get_width() / 4), int(img.get_height() / 4)))

    def draw(self):
        img = pygame.image.load(self.jo_counters[self.game.jo_counter])
        img = self.scale(img)
        img_rect = img.get_rect()
        img_rect.center = (SCREEN_WIDTH/2 + SCREEN_OFFSET, 55)
        self.game.screen.blit(img, img_rect.topleft)