"""
This program was written by Yonatan Deri.
"""
import pygame
from utils.consts import Constants

SIZE = 100
pygame.font.init()


def text_to_screen(screen, text: str, pos_x: int, pos_y: int, size=SIZE, color=Constants.WHITE.value,
                   font_type='Fonts/Tiny5-Regular.ttf') -> None:
    try:
        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (pos_x, pos_y))
    except Exception as e:
        print("Font Error.")
        raise e
