import pygame
import sys
from pygame.locals import *
from settings import *
from road import Road
from map import *
from gameui import Life
from collectible import Collectibles
from obstacle import Obstacle
from player import Player
from timer import Time
from bonus_jo import BonusJo
from overlay import Overlay
from gameover import GameOver
from pause import Pause
from levelup import LevelUp
from gamewin import GameWin
from utils import resource_path

import os

import time

class Game:
    def __init__(self):
        pygame.init()
        # self.screen = pygame.display.set_mode((SCREEN_OFFSET + SCREEN_WIDTH + SCREEN_OFFSET, SCREEN_HEIGHT))
        # pygame.display.set_caption("JoRunner")
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.scale_factor = self.screen.get_width() / (SCREEN_OFFSET + SCREEN_WIDTH + SCREEN_OFFSET)
        self.menu_width, self.menu_height = pygame.display.get_surface().get_size()

        # Frame count

        self.frame_count = 0

        # Player

        self.score = DEFAULT_SCORE
        self.lives = DEFAULT_LIVES
        self.player_hurt = False
        self.player_hurt_time = 60

        # Lines

        self.line_count = 0

        # Timer

        self.level_time = LEVEL_TIME
        self.level = 1
        self.remaining_time = self.level_time
        self.last_time = 0

        # Sound

        self.player_hit_sound = pygame.mixer.Sound(resource_path('assets/sounds/hurt.mp3'))
        pygame.mixer.init()
        # self.player_hit_sound = pygame.mixer.Sound(hurt_sound_path)

        self.level_sound = pygame.mixer.Sound(resource_path(f'assets/maps/{self.level}/music.mp3'))
        self.level_sound.set_volume(0.1)

        # Bonus Jo
        self.jo_counter = 0

        # Launch the game
        self.game_over = False
        self.is_game_win = False
        self.pause = False
        self.new_game()

    def new_game(self):
        self.create_road()
        self.reset_values()
        self.map = Map(self)
        self.player = Player(self)
        self.life = Life(self, self.lives)
        self.time = Time(self, self.level)
        self.BonusJo = BonusJo(self)
        self.overlay = Overlay(self)
        self.obstacles = []
        self.collectibles = []

    def reset_values(self):
        self.score = DEFAULT_SCORE
        self.lives = DEFAULT_LIVES
        self.player_hurt = False
        self.last_time = 0
        # self.jo_counter = 0
    
    def reset_level(self):
        self.level = 1
        self.level_time = LEVEL_TIME
        self.remaining_time = self.level_time

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                print("Pause")
                self.pause = not self.pause
                if self.pause:
                    self.pause_menu = Pause(self)
    def level_up(self, level):
        level_up = LevelUp(self, level)
        level_up.play()

    def create_road(self):
        self.road = Road(self)
        self.road_pos = 0
        self.road_acceleration = 80
        self.texture_position_acceleration = 4
        self.texture_position_threshold = 300
        self.half_texture_position_threshold = int(self.texture_position_threshold / 2)


    def update_road_position(self):
        self.road_pos += self.road_acceleration
        if self.road_pos >= self.texture_position_threshold:
            self.road_pos = 0
        self.road.texture_position = self.road_pos
        self.road.dz = 0
        self.road.z = 0

    def draw(self):
        self.screen.fill((255, 242, 204))
        self.road.draw(self.screen, self.road_pos, self.texture_position_acceleration,
                       self.texture_position_threshold, self.half_texture_position_threshold)
        self.map.draw()
        self.player.draw()
        self.life.draw()
        self.BonusJo.draw()

        

        for obstacle in self.obstacles:
            obstacle.draw()

        for collectible in self.collectibles:
            collectible.draw()


        self.player.update()

        self.overlay.draw()

        self.scale_factor = self.screen.get_height() / (SCREEN_HEIGHT)
        scaled_screen = pygame.transform.scale(self.screen,
                                           (int(self.screen.get_width() * self.scale_factor),
                                            int(self.screen.get_height() * self.scale_factor)))
        

        self.screen.fill((255, 242, 204))

        x_center = (self.menu_width - SCREEN_FULL_WIDTH * self.scale_factor) // 2
        print(x_center)


        self.screen.blit(scaled_screen, (x_center, 0))

        pygame.display.flip()   
        

    def get_obstacle(self):

        self.frame_count += 1
        current_time = int( pygame.time.get_ticks() / 1000)

        if current_time % (max(4 - self.level, 1)) == 0:
            if current_time != self.last_time:
                print("New obstacle")
                obstacle = Obstacle(self, random.randint(0, 2), 0)
                self.obstacles.append(obstacle)

        if current_time % 2 == 0:
            if current_time != self.last_time:
                print("New collectible")
                collectible = Collectibles(self, random.randint(0, 2), 0)
                self.collectibles.append(collectible)

        self.last_time = current_time

    def update_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.update()

    def update_collectibles(self):
        for collectible in self.collectibles:
            collectible.update()

    def disable_hurted_player(self):
        self.player_hurt = False

    def global_update(self):
        self.life.update()
        self.time.update_timer()

    def overlay_update(self):
        self.overlay.update()

    def run(self):
        self.level_sound.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)

            if not self.game_over:

                # print("Status: ", self.is_game_win)

                if self.pause:
                    self.pause_menu.draw()
                elif self.is_game_win:
                    self.game_win = GameWin(self)
                    self.game_win.draw()
                else:
                    self.handle_events()
                    self.update_road_position()
                    self.get_obstacle()
                    self.update_obstacles()
                    self.update_collectibles()
                    self.global_update()
                    self.overlay_update()
                    self.draw()

                    if self.lives == 0:
                        self.game_over = True
                        self.game_over_menu = GameOver(self)

            else:
                self.game_over_menu.draw()

            pygame.display.flip()