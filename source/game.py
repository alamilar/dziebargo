__author__ = 'Pawel'
import pygame


class game():
    def __init__(self, size=(640, 480)):
        pygame.init()
        self.screen = pygame.display.set_mode(size)


    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pygame.display.flip()
