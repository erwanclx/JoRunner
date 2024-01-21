import pygame
from settings import *
from utils import resource_path

class Overlay:
    def __init__(self, game):
        self.game = game
        self.wall = Wall(self.game)
        self.left_flame = Flame('left', self.game)
        self.right_flame = Flame('right', self.game)

        self.left_flag = Flag('left', self.game)
        self.right_flag = Flag('right', self.game)

    def draw(self):
        self.wall.draw()

        self.left_flame.draw('left')
        self.right_flame.draw('right')

        self.left_flag.draw('left')
        self.right_flag.draw('right')
        
    def update(self):
        self.left_flame.flame_frame()
        self.right_flame.flame_frame()

        self.left_flag.flag_frame()
        self.right_flag.flag_frame()

class Wall:
    def __init__(self, game):
        self.game = game
        self.texture = pygame.image.load(resource_path('assets/frame.png'))

        self.width = SCREEN_WIDTH
        self.height = 40
        self.x = SCREEN_OFFSET
        self.y = SCREEN_HEIGHT - self.height

        self.font = pygame.font.Font(resource_path('assets/fonts/pixel.ttf'), 20)
        
    def draw(self):
        self.game.screen.blit(pygame.transform.scale(self.texture, (self.width, self.height)), (self.x, self.y))
        text = self.font.render(f'Level {self.game.level}', True, (52, 53, 65))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH/2 + SCREEN_OFFSET, SCREEN_HEIGHT - 20)
        self.game.screen.blit(text, textRect)
class Flame:
    def __init__(self, orientation, game):
        self.flame_index = 1
        self.orientation = orientation
        self.game = game
        
        # Images
        self.orientations = {
            'left': pygame.image.load(resource_path(f'assets/overlay/flame/left/{self.flame_index}.png')),
            'right': pygame.image.load(resource_path(f'assets/overlay/flame/right/{self.flame_index}.png')),
        }

    def scale(self, img):
        return pygame.transform.scale(img, (int(img.get_width() / 1.5), int(img.get_height() / 1.5)))

    def flame_frame(self):
        if self.game.frame_count % 6 == 0:
            if self.flame_index == 1:
                self.flame_index = 2
            else:
                self.flame_index = 1
            self.orientations[self.orientation] = pygame.image.load(resource_path(f'assets/overlay/flame/{self.orientation}/{self.flame_index}.png'))
    
    def draw(self, orientation):
        if orientation == 'left':
            # self.game.screen.blit(self.orientations[orientation], (0, 100))
            img = self.scale(self.orientations[orientation])
            self.game.screen.blit(img, (SCREEN_OFFSET, SCREEN_HEIGHT - img.get_height()))
        else:
            # self.game.screen.blit(self.orientations[orientation], (SCREEN_WIDTH - 50, 100))
            img = self.scale(self.orientations[orientation])
            self.game.screen.blit(img, (SCREEN_FULL_WIDTH - SCREEN_OFFSET - img.get_width(), SCREEN_HEIGHT - img.get_height()))


class Flag:
    def __init__(self, orientation, game):
        self.orientation = orientation
        self.game = game

        self.flag_index = 1

        self.scale = 0.5

        self.orientations = {
            'left': pygame.image.load(resource_path(f'assets/overlay/flag/left/{self.flag_index}.png')),
            'right': pygame.image.load(resource_path(f'assets/overlay/flag/right/{self.flag_index}.png')),
        }

    def flag_frame(self):
        if self.game.frame_count % 6 == 0:
            if self.flag_index == 1:
                self.flag_index = 2
            else:
                self.flag_index = 1
            self.orientations[self.orientation] = pygame.image.load(resource_path(f'assets/overlay/flag/{self.orientation}/{self.flag_index}.png'))
    
    def draw(self, orientation):
        if orientation == 'left':
            self.game.screen.blit(self.orientations[orientation], (SCREEN_OFFSET + 220, 100))
        else:
            self.game.screen.blit(self.orientations[orientation], (SCREEN_FULL_WIDTH - 455, 100))