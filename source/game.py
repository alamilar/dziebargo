__author__ = 'Pawel'
import pygame


class game():
    def __init__(self, size=(600, 600)):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.load_assets()

    def load_assets(self):
        self.boardimage = pygame.image.load('assets/Plansza.bmp')

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.screen.blit(self.boardimage, (0,0))
            pygame.display.flip()
