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

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_OFFSET + SCREEN_WIDTH + SCREEN_OFFSET, SCREEN_HEIGHT))
        pygame.display.set_caption("JoRunner")
        self.road = Road()
        self.road_pos = 0
        self.road_acceleration = 80
        self.texture_position_acceleration = 4
        self.texture_position_threshold = 300
        self.half_texture_position_threshold = int(self.texture_position_threshold / 2)

        self.frame_count = 0

        self.score = DEFAULT_SCORE
        self.lives = DEFAULT_LIVES

        self.line_count = 0

        self.new_game()

    def new_game(self):
        self.reset_values()
        self.map = Map(self)
        self.player = Player(self)
        self.life = Life(self, self.lives)
        self.obstacles = []
        self.collectibles = []

    def reset_values(self):
        self.score = DEFAULT_SCORE
        self.lives = DEFAULT_LIVES

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_ESCAPE:
                # TODO: Pause the game
                pass


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

        for obstacle in self.obstacles:
            obstacle.draw()

        for collectible in self.collectibles:
            collectible.draw()
        

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

    def update_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.update()

    def update_collectibles(self):
        for collectible in self.collectibles:
            collectible.update()


    def life_check(self):
        if self.lives == 0 or self.lives < 0:
            self.new_game()
        if self.lives > MAX_LIVES:
            self.lives = MAX_LIVES

    def global_update(self):
        self.life.update()
        self.life_check()

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)
            self.handle_events()
            self.update_road_position()
            self.get_obstacle()
            self.update_obstacles()
            self.update_collectibles()
            self.global_update()
            self.draw()
            self.player.update()
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
