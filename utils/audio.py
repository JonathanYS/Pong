"""
This program was written by Yonatan Deri.
"""
import pygame


PONG_SOUND_EFFECT = "Audio/ping_pong_8bit_beeep.ogg"
MUSIC = "Audio/SunsetWalk.ogg"


class Audio:
    pygame.mixer.init()
    pygame.mixer.music.set_volume(10)

    @staticmethod
    def beep_sound():
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(PONG_SOUND_EFFECT))

    @staticmethod
    def play_music():
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(MUSIC), loops=-1)
