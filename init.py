import pygame
from colors import *
from config import *
from Player import *

# initialize pygame
pygame.init()

# initialize the sound
pygame.mixer.init()

# initialize the screen and set the sizes (from config.py)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set the caption (above the screen)
pygame.display.set_caption('First game')

# set the clock
clock = pygame.time.Clock()
