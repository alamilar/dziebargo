import pygame
from constants import Player_Colors
from field import Field

class Board:
    margin = 10
    balloffset = 60
    def __init__(self, board):

        self.board = [[x for x in range(9)] for x in range(9)]
        for x in range(9):
            for y in range(9):
                self.board[x][y] =  Field(Player_Colors.Undetermined, (600/9*x+12 , 600/9*y+12))
        self.boardimage = board.boardimage
        self.screen = board.screen
        self.boardwsk = board

    def render(self):
        self.screen.blit(self.boardimage, (0,0))
        for row in self.board:
            for field in row:
                self.screen.blit(self.boardwsk.players_ball[field.color], field.position)

    def handle_mouse(self, position):
        for row in self.board:
            for field in row:
                if field.rect.collidepoint(position[0], position[1]):
                    print 'Nacisnieto na pozycji ' + str(field.coords[0]) + ' ' + str(field.coords[1])
                    field.color = (field.color + 1) % 5
