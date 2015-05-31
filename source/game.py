# coding=utf-8
import pygame
from source.board import Board
from source.loger import log
from source.player import Player
from source.constants import *
import sys


class Game(object):
    '''
    Główna klasa odpowiedzialna za obsługę gry, zawiera obsługę turowości, pomaga ogarniać obiekt Board
    '''
    def __init__(self, players_number,  size=(600, 650)):
        log("================ NEW RUNME")
        try:
            pygame.init()
            self.screen = pygame.display.set_mode(size)
        except Exception as e:
            log(str(e), "ERR")
            raise Exception




        self.board_image = None
        self.players_ball = None
        self.load_assets()

        self.setup_players(players_number)
        self.tour = Beginning

        self.board = Board(self)

    def setup_players(self, players_number):
        '''
        Służy do tworzenia tablicy graczy, i inicjalizacji zmiennych do obsługi tur
        :param players_number:
        :return:
        '''
        self.players_number = players_number
        self.current_player = 1
        self.players = []
        for _ in range(players_number):
            self.players.append(Player(_+1, self.players_ball[_+1]))

    def load_assets(self):
        '''
        Służy do ładowania plików graficznych
        :return:
        '''

        try:
            self.board_image = pygame.image.load('assets/background.bmp').convert()
            self.players_ball = (
                pygame.image.load('assets/ball_empty.gif'),
                pygame.image.load('assets/ball_red.gif'),
                pygame.image.load('assets/ball_blue.gif'),
                pygame.image.load('assets/ball_green.gif'),
                pygame.image.load('assets/ball_pink.gif'),
                pygame.image.load('assets/ball_yellow.gif')
            )
        except Exception as e:
            log(str(e), "ERR")
            raise Exception

    def next_player(self):
        '''
        Służy do przełączania tury
        :return:
        '''
        self.current_player += 1
        if self.current_player > self.players_number:
            self.current_player = 1

    def main_loop(self):
        '''
        Główna funkcja służąca do obsługi pętli gry
        :return:
        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP and self.tour == Beginning:
                    print 'Gracz numer ' + str(self.current_player)
                    pos = pygame.mouse.get_pos()
                    if self.board.handle_mouse(pos, self.players[self.current_player-1]):
                        self.tour = Middle
                if event.type == pygame.KEYDOWN and self.tour == Middle:
                    self.board.handle_key(event.key)
                    print 'Koniec tury gracza ' + str(self.current_player)
                    self.next_player()
                    self.tour = Beginning
            self.board.render()
            font = pygame.font.Font(None, 36)
            textpos = pygame.Rect(150, 615, 100, 100)
            self.screen.fill((255, 255, 255), pygame.Rect(0, 600, 600, 200))
            if self.tour == Beginning:
                text = font.render("Graczu " + str(self.current_player) + " poloz pionek", 1, (15, 15, 15))
            else:
                text = font.render("Graczu " + str(self.current_player) + " obroc plansze", 1, (15, 15, 15))
            self.screen.blit(text, textpos)
            pygame.time.wait(100)
            pygame.display.flip()
