"""
This program was written by Yonatan Deri.
"""
import pygame
from enum import Enum


class Constants(Enum):
    # RGB values
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    WIDTH, HEIGHT = 1000, 750
    SCREEN = pygame.display.set_mode((1000, 750))

    CLOCK = pygame.time.Clock()
    FPS = 60
