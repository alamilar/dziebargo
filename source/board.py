# coding=utf-8
import pygame
from source.Loger import log
from source.constants import *
from source.field import Field


class Board:
    def __init__(self, game):
        self.board = [
            [
                Field(game.players_ball[0], (600 / 9 * x + 12, 600 / 9 * y + 12))
                for x in range(9)
                ]
            for y in range(9)
            ]
        log("Map array created")
        self.board_image = game.board_image
        self.screen = game.screen
        self.game = game

    def render(self):
        '''
        Funkcja renderująca plansze i pionki
        :return:
        '''
        self.screen.blit(self.board_image, (0, 0))
        for row in self.board:
            for field in row:
                self.screen.blit(field.color, field.position)

    def handle_mouse(self, position, player):
        '''
        Funkcja do obsługi stawiania pionków
        :param position:
        :param player:
        :return:
        '''
        log("handle mouse: (%s,%s)" % (position[0], position[1]))
        for row in self.board:
            for field in row:
                if field.rect.collidepoint(position[0], position[1]):
                    log('Mouse collision:' + str(field.cords[0]) + ' ' + str(field.cords[1]))
                    field.color = player.color
                    return True
        return False

    def handle_key(self, key):
        '''
        Funkcja do obsługi obracania
        :param key:
        :return:
        '''
        log("handle key: %s" % key)
        if key == pygame.K_1:
            self.rotate_right(1, 1)
        if key == pygame.K_q:
            self.rotate_left(1, 1)

        if key == pygame.K_2:
            self.rotate_right(1, 4)
        if key == pygame.K_w:
            self.rotate_left(1, 4)

        if key == pygame.K_3:
            self.rotate_right(1, 7)
        if key == pygame.K_e:
            self.rotate_left(1, 7)

        if key == pygame.K_4:
            self.rotate_right(4, 1)
        if key == pygame.K_r:
            self.rotate_left(4, 1)

        if key == pygame.K_5:
            self.rotate_right(4, 4)
        if key == pygame.K_t:
            self.rotate_left(4, 4)

        if key == pygame.K_6:
            self.rotate_right(4, 7)
        if key == pygame.K_y:
            self.rotate_left(4, 7)

        if key == pygame.K_7:
            self.rotate_right(7, 1)
        if key == pygame.K_u:
            self.rotate_left(7, 1)

        if key == pygame.K_8:
            self.rotate_right(7, 4)
        if key == pygame.K_i:
            self.rotate_left(7, 4)

        if key == pygame.K_9:
            self.rotate_right(7, 7)
        if key == pygame.K_o:
            self.rotate_left(7, 7)

    def rotate_right(self, x, y):
        '''
        Funkcja obracająca zadnany blok w prawo
        :param x:
        :param y:
        :return:
        '''
        for _ in xrange(0, 2):
            self.move_one(x, y)

    def rotate_left(self, x, y):
        '''
        Funkcja obracająca zadnany blok w lewo
        :param x:
        :param y:
        :return:
        '''
        for _ in xrange(0, 6):
            self.move_one(x, y)

    def move_one(self, x, y):
        '''
        Przekształcenia na bloku powodujące przemieszczenie pionków
        :param x:
        :param y:
        :return:
        '''
        tmp = self.board[x - 1][y - 1].color
        self.board[x - 1][y - 1].color = self.board[x][y - 1].color
        self.board[x][y - 1].color = self.board[x + 1][y - 1].color
        self.board[x + 1][y - 1].color = self.board[x + 1][y].color
        self.board[x + 1][y].color = self.board[x + 1][y + 1].color
        self.board[x + 1][y + 1].color = self.board[x][y + 1].color
        self.board[x][y + 1].color = self.board[x - 1][y + 1].color
        self.board[x - 1][y + 1].color = self.board[x - 1][y].color
        self.board[x - 1][y].color = tmp

    def lines_with_point(x, y):
        return (
            "|;"+str(x),
            "-;"+str(y),
            "/;"+str(x-y),
            "\\;"+str(x-y)
        )

    def check_if_is_five_in_line(self, line_desc):
        line = get_line(line_desc)



    def check_if_five_for_point(self, *points):
        list_of_linies = {}
        for point in points:
            list_of_linies.pop(self.lines_with_point(point))
        for line in list_of_linies:
            status = self.check_if_is_five_in_line(line)
            if status is not None:
                return status
        return None
