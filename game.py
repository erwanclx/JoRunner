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

import time

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_OFFSET + SCREEN_WIDTH + SCREEN_OFFSET, SCREEN_HEIGHT))
        pygame.display.set_caption("JoRunner")

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

        # Sound

        self.player_hit_sound = pygame.mixer.Sound('assets/sounds/hurt.mp3')

        # Bonus Jo
        self.jo_counter = 0

        # Launch the game
        self.game_over = False
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
        self.jo_counter = 0
    
    def reset_level(self):
        self.level = 1
        self.level_time = LEVEL_TIME
        self.remaining_time = self.level_time

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_ESCAPE:
                # TODO: Pause the game
                pass

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
        

    def get_obstacle(self):

        if self.frame_count % 6 == 0:
                if not random.randint(0,2):

                    if not random.randint(0, 4):
                        collectible = Collectibles(self, random.randint(0, 2), 0)
                        self.collectibles.append(collectible)
                    else:
                        if self.line_count % 4 == 0:
                            obstacle = Obstacle(self, random.randint(0, 2), 0)
                            self.obstacles.append(obstacle)
                        self.line_count += 1
        self.frame_count += 1
        # Instead of frame use clock
        # All the 3 seconds make a new obstacle
        # All the 5 seconds make a new collectible
    #     current_time = pygame.time.get_ticks()

    #     # Every 3000 milliseconds (3 seconds), create a new obstacle
    #     if current_time % 3000 == 0:
    #         obstacle = Obstacle(self, random.randint(0, 2), 0)
    #         self.obstacles.append(obstacle)

    # # Every 5000 milliseconds (5 seconds), create a new collectible
    #     if current_time % 5000 == 0:
    #         collectible = Collectibles(self, random.randint(0, 2), 0)
    #         self.collectibles.append(collectible)

    def update_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.update()

    def update_collectibles(self):
        for collectible in self.collectibles:
            collectible.update()

    def disable_hurted_player(self):
        self.player_hurt = False

    # def life_check(self):
    #     if self.lives == 0 or self.lives < 0:
    #         # self.new_game()
    #         self.game_over = GameOver(self)
    #         self.game_over.draw()
    #         # pygame.display.flip()

    #     if self.lives > MAX_LIVES:
    #         self.lives = MAX_LIVES

    def global_update(self):
        self.life.update()
        # self.life_check()
        self.time.update_timer()
        # self.disable_hurted_player()

    def overlay_update(self):
        self.overlay.update()

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)
            if not self.game_over:
                self.handle_events()
                self.update_road_position()
                self.get_obstacle()
                self.update_obstacles()
                self.update_collectibles()
                self.global_update()
                self.overlay_update()
                self.draw()
                pygame.display.flip()

                if self.lives == 0:
                    self.game_over = True
                    self.game_over = GameOver(self)
                    self.game_over.draw()
            else:
                self.game_over.draw()
                pygame.display.flip()

# if __name__ == "__main__":
#     game = Game()
#     game.run()
