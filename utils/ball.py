"""
This program was written by Yonatan Deri.
"""
import pygame.draw
import random

from utils.consts import Constants
from utils.audio import Audio


class Ball:
    def __init__(self, radius: int, pos_x: int, pos_y: int, speed: int, color: tuple):
        self.radius = radius
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.color = color
        self.first_hit = 1

        self.first_speed = speed
        self.first_max_collisions = 35

        self.total_collisions = 0
        self.max_collisions = self.first_max_collisions

        self.x_status = 1  # go right.
        self.y_status = -1  # go up.

        # First drawing of the ball.
        self.ball = pygame.draw.circle(Constants.SCREEN.value, self.color, (self.pos_x, self.pos_y), self.radius)

    def draw(self) -> None:
        self.ball = pygame.draw.circle(Constants.SCREEN.value, self.color, (self.pos_x, self.pos_y), self.radius)

    def move(self) -> int:
        pygame.draw.circle(Constants.SCREEN.value, Constants.BLACK.value, (self.pos_x, self.pos_y), self.radius)
        self.pos_y += self.speed * self.y_status
        self.pos_x += self.speed * self.x_status

        if self.pos_y <= 10 or self.pos_y >= Constants.HEIGHT.value - 10:
            self.y_status = -self.y_status

        if self.pos_x <= 10 and self.first_hit:
            self.first_hit = 0
            return 1
        if self.pos_x >= Constants.WIDTH.value - 10 and self.first_hit:
            self.first_hit = 0
            return -1
        return 0

    def restart(self) -> None:
        self.pos_x = Constants.WIDTH.value // 2
        self.pos_y = Constants.HEIGHT.value // 2
        self.x_status = -self.x_status  # So that the ball would go to the scorer side.
        self.y_status = random.choice([i for i in range(-1, 1) if i != 0])
        self.first_hit = 1
        self.speed = self.first_speed
        self.total_collisions = 0
        self.max_collisions = self.first_max_collisions

    def collision(self) -> None:
        self.total_collisions += 1
        self.x_status = -self.x_status
        Audio.beep_sound()
        if self.total_collisions >= self.max_collisions:
            self.speed *= 1.25
            self.max_collisions *= 2

    def get_rect(self) -> pygame.Rect:
        return self.ball
