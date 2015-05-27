# coding=utf-8
import pygame
from board import Board
from Loger import log


class Game(object):
    def __init__(self, size=(600, 600), players_number=2):
        try:
            pygame.init()
            self.screen = pygame.display.set_mode(size)
        except Exception as e:
            log(str(e), "CRIT")
            raise Exception
        self.players_number = players_number
        self.current_player = 1
        self.boardimage = None
        self.players_ball = None
        self.load_assets()
        self.board = Board(self)

    def load_assets(self):

        try:
            self.boardimage = pygame.image.load('assets/background.bmp').convert()
            self.players_ball = (
                pygame.image.load('assets/ball_empty.gif'),
                pygame.image.load('assets/ball_red.gif'),
                pygame.image.load('assets/ball_blue.gif'),
                pygame.image.load('assets/ball_green.gif'),
                pygame.image.load('assets/ball_pink.gif'),
                pygame.image.load('assets/ball_yellow.gif')
            )
        except Exception as e:
            log(str(e), "CRIT")
            raise Exception

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
                if event.type == pygame.KEYDOWN:
                    self.board.handle_key(event.key)

            '''
            Renderowanie
            '''
            self.board.render()
            pygame.time.wait(100)
            pygame.display.flip()
