"""
This program was written by Yonatan Deri.
"""
import pygame
from utils.consts import Constants


class Player:
    def __init__(self, speed: int, color: tuple, pos_x: int, pos_y: int, width: int, height: int):
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.player_rect = pygame.Rect(pos_x, pos_y, width, height)

        # First drawing of the player.
        self.player = pygame.draw.rect(Constants.SCREEN.value, self.color, self.player_rect)

    def draw(self) -> None:
        self.player = pygame.draw.rect(Constants.SCREEN.value, self.color, self.player_rect)

    def move(self, y_status) -> None:
        self.pos_y = self.pos_y + self.speed * y_status

        if self.pos_y <= 10:
            self.pos_y = 10
        elif self.pos_y + self.height >= Constants.HEIGHT.value - 10:
            self.pos_y = Constants.HEIGHT.value - self.height - 10

        # Draw over the existing rectangle with the color of the background (in this case, black).
        pygame.draw.rect(Constants.SCREEN.value, Constants.BLACK.value, self.player_rect)
        self.player_rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def get_rect(self) -> pygame.Rect:
        return self.player_rect
