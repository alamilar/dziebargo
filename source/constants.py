# coding=utf-8
# pylint: disable=no-member
"""
Constants
"""


import pygame

UNDETERMINED, RED, GREEN, YELLOW, BLUE = range(0, 5)
BEGINING, MIDLE = 1, 2

TEXT_MENU = """
    Welcome in Game
    press key:
    1 start game for 1 player
    2 start game for 2 players
    3 start game for 2 players
    q quit
    """

LOG_LEVEL = "none"

KEYS = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
        pygame.K_8, pygame.K_9, pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t,
        pygame.K_y, pygame.K_u, pygame.K_i, pygame.K_o]
