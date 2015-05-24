from constants import Player_Colors
from field import Field

class Board:
    margin = 10
    balloffset = 60
    def __init__(self, boardimage, colors, numberofplayers):
        self.board = [[x for x in range(9)] for x in range(9)]
        for x in range(9):
            for y in range(9):
                self.board[x][y] = Field(Player_Colors.Undetermined, (self.margin + self.balloffset * x, self.balloffset * y + self.margin))