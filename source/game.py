# coding=utf-8
# pylint: disable=deprecated-lambda
# pylint: disable=bad-builtin
# pylint: disable=cell-var-from-loop
# pylint: disable=invalid-name
# pylint: disable=undefined-variable
# pylint: disable=wildcard-import
# pylint: disable=import-error
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes
"""
class Game
"""

from source.board import Board
from source.loger import log
from source.player import Player
from source.constants import *


class Game(object):
    """
    Główna klasa odpowiedzialna za obsługę gry, zawiera
    obsługę turowości, pomaga ogarniać obiekt Board
    """

    def __init__(self, players_number, size=(600, 650)):
        log("================ NEW RUNME")
        try:
            pygame.init()
            self.screen = pygame.display.set_mode(size)
        except Exception as e:
            log(str(e))
            raise Exception

        self.count_of_colored_field = 0
        self.board_image = None
        self.players_ball = None
        self.load_assets()
        self.winners = ""

        self.players_number = players_number
        self.current_player = 1
        self.players = []
        for _ in range(players_number):
            self.players.append(Player(_ + 1))
        self.per_move_flag = True
        self.tour = BEGINING

        self.board = Board(self)

    def load_assets(self):
        """
        Służy do ładowania plików graficznych
        :return:
        """

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
            log(str(e))
            raise Exception

    def next_player(self):
        """
        Służy do przełączania tury
        :return:
        """
        self.current_player += 1
        if self.current_player > self.players_number:
            self.current_player = 1

    def main_loop(self):
        """
        Główna funkcja służąca do obsługi pętli gry
        :return:
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "End by cross."
                if event.type == pygame.MOUSEBUTTONUP and self.tour == BEGINING:
                    self.per_move_flag = True
                    print 'Gracz numer ' + str(self.current_player)
                    pos = pygame.mouse.get_pos()
                    if self.board.handle_mouse(pos, self.players[self.current_player - 1]):
                        self.tour = MIDLE
                if event.type == pygame.KEYDOWN and self.tour == MIDLE and event.key in KEYS:
                    self.per_move_flag = True
                    self.board.handle_key(event.key)
                    print 'Koniec tury gracza ' + str(self.current_player)
                    self.next_player()
                    self.tour = BEGINING
            if self.count_of_colored_field == 81:
                pygame.quit()
                return "Koniec gry - remis"
            if self.per_move_flag:
                self.per_move_flag = False
                if self.check_win():
                    pygame.quit()
                    return "Koniec gry - wygral: %s " % self.winners

            self.board.render()
            font = pygame.font.Font(None, 36)
            textpos = pygame.Rect(150, 615, 100, 100)
            self.screen.fill((255, 255, 255), pygame.Rect(0, 600, 600, 200))
            if self.tour == BEGINING:
                text = font.render("Graczu " + str(self.current_player)\
                                   + " poloz pionek", 1, (15, 15, 15))
            else:
                text = font.render("Graczu " + str(self.current_player)\
                                   + " obroc plansze", 1, (15, 15, 15))
            self.screen.blit(text, textpos)
            pygame.time.wait(100)
            pygame.display.flip()

    def check_win(self):
        """
        chcek if any one win
        :return:
        """
        fx = range(0, 9)
        f0 = [0 for _ in range(0, 9)]

        def list_(*args):
            """
            make list fron args
            """
            return list(args)

        def zip_(*args):
            """
            make list fron args
            """
            return map(list_, *args)

        row_template = zip_(fx, f0)
        col_template = zip(f0, fx)
        hor_template = zip(fx, fx)
        hor2_template = zip(fx, fx[::-1])

        list_of_lines = []

        for i in fx:
            tmp = map(lambda p: (p[0], p[1] + i), row_template)
            list_of_lines.append(tmp)

        for i in fx:
            tmp = map(lambda p: (p[0] + i, p[1]), col_template)
            list_of_lines.append(tmp)

        for i in fx:
            tmp = map(lambda p: (p[0] + i, p[1]), hor_template)
            list_of_lines.append(tmp)

        for i in fx:
            tmp = map(lambda p: (p[0], p[1] + i), hor_template)
            list_of_lines.append(tmp)

        for i in fx:
            tmp = map(lambda p: (p[0] + i, p[1]), hor2_template)
            list_of_lines.append(tmp)

        for i in fx:
            tmp = map(lambda p: (p[0], p[1] - i), hor2_template)
            list_of_lines.append(tmp)

        for _ in xrange(0, 9):
            for line in list_of_lines:
                for elem in line:
                    if (elem[0] >= 9) or (elem[1] >= 9) or (elem[0] < 0) or (elem[1] < 0):
                        line.remove(elem)

        for line in list_of_lines:
            self.check_line(line)
        if self.winners:
            return True
        else:
            return False

    def check_line(self, temp):
        """
        check line for line color
        :param temp:
        :return:
        """
        prev = -1
        counter = 0
        line = (
            self.board.board[temp[i][0]][temp[i][1]] for i in range(0, len(temp))
        )

        for poz in line:
            if prev == poz.color:
                counter += 1
            else:
                counter = 0
                prev = poz.color
            if prev == 0:
                counter = 0
            if counter:
                print counter,
            if counter == 4:
                counter = 0
                self.winners += str(prev) + " "

