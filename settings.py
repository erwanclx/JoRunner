import pygame

# Screen settings | Coresponding to the road texture size

ASSETS_MULTIPLIER = 1
SCREEN_WIDTH = int(803 * ASSETS_MULTIPLIER)
SCREEN_HEIGHT = int(672 * ASSETS_MULTIPLIER)
SCREEN_OFFSET = int(160 * ASSETS_MULTIPLIER)
SCREEN_FULL_WIDTH = SCREEN_WIDTH + SCREEN_OFFSET + SCREEN_OFFSET

# SCREEN_WIDTH = 1920
# SCREEN_HEIGHT = 1080
# SCREEN_FULL_WIDTH = SCREEN_WIDTH
# SCREEN_OFFSET = 0

HALF_SCREEN_HEIGHT=int(SCREEN_HEIGHT/2)

PLAYABLE_SCREEN_HEIGHT = int(SCREEN_HEIGHT/3) * 2

# Grid settings
TILE_ROWS=5
TILE_COLUMNS=4
TILES_TOTAL=TILE_ROWS*TILE_COLUMNS
TILE_SIZE= PLAYABLE_SCREEN_HEIGHT/TILE_ROWS
# TILE_SIZE= HALF_SCREEN_HEIGHT/TILE_ROWS
TILE_HEIGHT=PLAYABLE_SCREEN_HEIGHT/TILE_COLUMNS
# TILE_HEIGHT=HALF_SCREEN_HEIGHT/TILE_COLUMNS
TILE_WIDTH=SCREEN_WIDTH/3

FPS = 20


ICONS_SIZE = 64 * ASSETS_MULTIPLIER

# Player
PLAYER_POSITION = 1
HORIZONTAL_SPEED = 50

DEFAULT_LIVES = 3
MAX_LIVES = 3
DEFAULT_SCORE = 0

# Game settings
LEVEL_TIME = 60
# SCORE_TO_CHANGE_LEVEL = 1
SCORE_TO_CHANGE_LEVEL = 1
LEVEL_NUMBER = 5



DEBUG = False