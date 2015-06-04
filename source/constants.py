import pygame

Undetermined, Red, Green, Yellow, Blue = range(0, 5)
Beginning, Middle = 1, 2
horizontal_lines = []
vertical_lines = []
rising_lines = []
falling_lines = []
text_menu = """
    Welcome in Game
    press key:
    1 start game for 1 player
    2 start game for 2 players
    3 start game for 2 players
    q quit
    """

debug = True

keys = [pygame.K_1, pygame.K_2, pygame.K_3 ,pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8 ,pygame.K_9,
        pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t, pygame.K_y, pygame.K_u, pygame.K_i, pygame.K_o  ]