import pygame

class ScaledContent():
    def __init__(self, game, source):
        self.game = game
        self.source = source
        self.aspect_ratio = self.game.menu_width / self.game.menu_height
        self.new_width = int(self.game.menu_height * self.aspect_ratio)
        self.new_height = self.game.menu_height