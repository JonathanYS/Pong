"""
This program was written by Yonatan Deri.
"""
import pygame
from utils.consts import Constants


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.current_option = 0

    def display_image(self, img_path: str, pos_x: int, pos_y: int):
        self.screen.fill(Constants.BLACK.value)
        if img_path == "Images/retry_option.png":
            self.current_option = 0
        elif img_path == "Images/exit_option.png":
            self.current_option = 1
        elif img_path == "Images/start_option.png":
            self.current_option = 2
        elif img_path == "Images/exit_at_start_menu.png":
            self.current_option = 3
        img = pygame.image.load(img_path).convert()
        self.screen.blit(img, (pos_x, pos_y))

    def get_option(self):
        return self.current_option
