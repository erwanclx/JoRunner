import pygame
from settings import *

# Half image
# class Road:
#     def __init__(self):
#         self.light_road = pygame.image.load('assets/light_road.medium.png').convert()
#         # self.light_road = pygame.image.load('assets/light_road.old.png').convert()
#         self.dark_road = pygame.image.load('assets/dark_road.medium.png').convert()
#         # self.dark_road = pygame.image.load('assets/dark_road.old.png').convert()
#         self.texture_position = 0
#         self.ddz = 0.001
#         self.dz = 0
#         self.z = 0
#     def draw(self, screen, road_pos, texture_position_acceleration, texture_position_threshold, half_texture_position_threshold):
#         screen.fill((0,0,255))
#         for i in range(HALF_SCREEN_HEIGHT-1, -1, -1):
#             if self.texture_position < half_texture_position_threshold:
#                 screen.blit(self.light_road, (0, i+HALF_SCREEN_HEIGHT), (0, i, SCREEN_WIDTH, 1))
#             else:
#                 screen.blit(self.dark_road, (0, i+HALF_SCREEN_HEIGHT), (0, i, SCREEN_WIDTH, 1))
#             self.dz += self.ddz
#             self.z += self.dz

#             self.texture_position += texture_position_acceleration + self.z
#             if self.texture_position >= texture_position_threshold:
#                 self.texture_position = 0

# Full image

# class Road:
#     def __init__(self):
#         self.light_road = pygame.image.load('assets/light_road.png').convert()
#         self.dark_road = pygame.image.load('assets/dark_road.png').convert()
#         self.texture_position = 0
#         self.ddz = 0.001
#         self.dz = 0
#         self.z = 0

#     def draw(self, screen, road_pos, texture_position_acceleration, texture_position_threshold, half_texture_position_threshold):
#         screen.fill((255, 242, 204))
#         for i in range(SCREEN_HEIGHT-1, -1, -1):
#             if self.texture_position < half_texture_position_threshold:
#                 screen.blit(self.light_road, (0, i), (0, i, SCREEN_WIDTH, 1))
#             else:
#                 screen.blit(self.dark_road, (0, i), (0, i, SCREEN_WIDTH, 1))
#             self.dz += self.ddz
#             self.z += self.dz

#             self.texture_position += texture_position_acceleration + self.z
#             if self.texture_position >= texture_position_threshold:
#                 self.texture_position = 0

# Add Road centered on screen
class Road:
    def __init__(self, game):
        self.game = game
        self.light_road = pygame.image.load(f'assets/maps/{self.game.level}/1B.png').convert()
        # self.light_road = pygame.image.load(f'assets/maps/{self.game.level}/1.png').convert()
        self.dark_road = pygame.image.load(f'assets/maps/{self.game.level}/1A.png').convert()
        # self.dark_road = pygame.image.load(f'assets/maps/{self.game.level}/2.png').convert()
        self.light_road = pygame.transform.scale(self.light_road, (SCREEN_FULL_WIDTH, SCREEN_HEIGHT))
        self.dark_road = pygame.transform.scale(self.dark_road, (SCREEN_FULL_WIDTH, SCREEN_HEIGHT))
        self.texture_position = 0
        self.ddz = 0.001
        self.dz = 0
        self.z = 0

    def draw(self, screen, road_pos, texture_position_acceleration, texture_position_threshold, half_texture_position_threshold):
        screen.fill((255, 242, 204))
        for i in range(SCREEN_HEIGHT-1, -1, -1):
            if self.texture_position < half_texture_position_threshold:
                # screen.blit(self.light_road, (SCREEN_OFFSET, i), (0, i, SCREEN_WIDTH, 1))
                screen.blit(self.light_road, (0, i), (0, i, SCREEN_FULL_WIDTH, 1))
            else:
                # screen.blit(self.dark_road, (SCREEN_OFFSET, i), (0, i, SCREEN_WIDTH, 1))
                screen.blit(self.dark_road, (0, i), (0, i, SCREEN_FULL_WIDTH, 1))
            self.dz += self.ddz
            self.z += self.dz

            self.texture_position += texture_position_acceleration + self.z
            if self.texture_position >= texture_position_threshold:
                self.texture_position = 0