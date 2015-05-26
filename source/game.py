# coding=utf-8
import pygame
from board import Board


class game():
    def __init__(self, size=(600, 600), players_number=2):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.load_assets()
        self.init_things()
        self.players_number = [range(1,players_number+1)]

    def load_assets(self):
        self.boardimage = pygame.image.load('assets/Plansza.bmp').convert()
        self.players_ball = (
            pygame.image.load('assets/pionekempty.gif'),
            pygame.image.load('assets/ball_red.gif'),
            pygame.image.load('assets/ball_blue.gif'),
            pygame.image.load('assets/ball_red.gif'),
            pygame.image.load('assets/ball_green.gif'),
            pygame.image.load('assets/ball_yellow.gif')
        )
 
    def init_things(self):
        self.board = Board(self)

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
