import pygame
from settings import *

class Overlay:
    def __init__(self, game):
        self.game = game
        self.wall = Wall(self.game)
        self.left_flame = Flame('left', self.game)
        self.right_flame = Flame('right', self.game)

    def draw(self):
        self.wall.draw()

        self.left_flame.draw('left')
        self.right_flame.draw('right')
    def update(self):
        self.left_flame.flame_frame()
        self.right_flame.flame_frame()

class Wall:
    def __init__(self, game):
        self.game = game
        self.texture = pygame.image.load('assets/frame.png')

        self.width = SCREEN_WIDTH
        self.height = 40
        self.x = SCREEN_OFFSET
        self.y = SCREEN_HEIGHT - self.height

        self.font = pygame.font.Font('assets/fonts/pixel.ttf', 20)
        
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
            'left': pygame.image.load(f'assets/overlay/flame/left/{self.flame_index}.png'),
            'right': pygame.image.load(f'assets/overlay/flame/right/{self.flame_index}.png'),
        }

    def flame_frame(self):
        if self.game.frame_count % 6 == 0:
            if self.flame_index == 1:
                self.flame_index = 2
            else:
                self.flame_index = 1
            self.orientations[self.orientation] = pygame.image.load(f'assets/overlay/flame/{self.orientation}/{self.flame_index}.png')
    
    def draw(self, orientation):
        if orientation == 'left':
            self.game.screen.blit(self.orientations[orientation], (0, 100))
        else:
            self.game.screen.blit(self.orientations[orientation], (SCREEN_WIDTH - 50, 100))