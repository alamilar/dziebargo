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



        self.count_of_colored_field = 0
        self.board_image = None
        self.players_ball = None
        self.load_assets()
        self.winners = ""

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
            self.players.append(Player(_+1))
        self.per_move_flag = True

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
            self.press_sound = pygame.mixer.Sound('assets/button.wav')
            self.move_sound = pygame.mixer.Sound('assets/move.wav')
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
                    pygame.quit()
                    return "End by cross."
                if event.type == pygame.MOUSEBUTTONUP and self.tour == Beginning:
                    self.per_move_flag = True
                    print 'Gracz numer ' + str(self.current_player)
                    pos = pygame.mouse.get_pos()
                    if self.board.handle_mouse(pos, self.players[self.current_player-1]):
                        self.tour = Middle
                        self.press_sound.play()
                if event.type == pygame.KEYDOWN and self.tour == Middle and event.key in keys:
                    self.per_move_flag = True
                    self.board.handle_key(event.key)
                    print 'Koniec tury gracza ' + str(self.current_player)
                    self.next_player()
                    self.tour = Beginning
                    self.move_sound.play()
            if self.count_of_colored_field == 81:
                return "Koniec gry - remis"
            if self.per_move_flag:
                self.per_move_flag = False
                if self.check_win():
                    return "Koniec gry - wygral: %s " % self.winners

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

    def check_win(self):
        fx = range(0,9)
        f0 = [0 for _ in range(0,9)]

        def list_(*args):
            return list(args)
        def zip_(*args):
            return map(list_, *args)
        row_template = zip_(fx, f0)
        col_template = zip(f0, fx)
        hor_template = zip(fx, fx)

        list_of_lines = []

        for i in fx:
            tmp = map(lambda p: (p[0], p[1]+i), row_template)
            list_of_lines.append(tmp)

        for i in fx:
            tmp = map(lambda p: (p[0]+i, p[1]), col_template)
            list_of_lines.append(tmp)

        for line in list_of_lines:
            self.check_line(line)
        if self.winners:
            return True
        else:
            return False

    def check_line(self, temp):
        prev = -1
        counter = 0
        line = (
            self.board.board[temp[i][0]][temp[i][1]] for i in range(0, 9)
        )

        for x in line:
            if prev == x.color:
                counter += 1
            else:
                counter = 0
                prev = x.color
            if prev == 0:
                counter = 0
            if counter:
                print counter,
            if counter == 3:
                counter = 0
                self.winners += str(prev) + " "

