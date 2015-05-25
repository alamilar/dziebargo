# coding=utf-8
import pygame
from board import Board


class game():
    def __init__(self, size=(600, 600)):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.load_assets()
        self.init_things()
        self.players = [1, 2]

    def load_assets(self):
        self.boardimage = pygame.image.load('assets/Plansza.bmp').convert()
        self.redimage = pygame.image.load('assets/pionek.gif')
        self.greenimage = pygame.image.load('assets/pionek.gif')
        self.emptyimage = pygame.image.load('assets/pionekempty.gif')

    def init_things(self):
        self.board = Board((self.boardimage, self.screen), (self.emptyimage, self.redimage, self.greenimage), 2)

    def main_loop(self):

        while True:
            '''
            Przetwarzanie eventów
            '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.board.handle_mouse(pos)
                    print pos


            '''
            Renderowanie
            '''
            self.board.render()
            pygame.time.wait(100)
            pygame.display.flip()
