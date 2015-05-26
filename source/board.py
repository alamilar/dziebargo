import pygame
from constants import Player_Colors
from field import Field

class Board:
    def __init__(self, board):
        self.board = [
                        [
                            Field(Player_Colors.Undetermined, (600/9*x+12 , 600/9*y+12)) 
                            for x in range(9)
                        ] 
                        for y in range(9)
                ]
       
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
                    field.color = self.boardwsk.current_player
                    self.boardwsk.current_player += 1
                    if self.boardwsk.current_player > self.boardwsk.players_number:
                        self.boardwsk.current_player = 1
                    
    def handle_key(self, key):
    
        if(key==pygame.K_1):
            self.rotate_right(1,1)
        if(key==pygame.K_q):
            self.rotate_left(1,1)
            
        if(key==pygame.K_2):
            self.rotate_right(1,4)
        if(key==pygame.K_w):
            self.rotate_left(1,4)
            
        if(key==pygame.K_3):
            self.rotate_right(1,7)
        if(key==pygame.K_e):
            self.rotate_left(1,7)
            
        if(key==pygame.K_4):
            self.rotate_right(4,1) 
        if(key==pygame.K_r):
            self.rotate_left(4,1)
            
        if(key==pygame.K_5):
            self.rotate_right(4,4)
        if(key==pygame.K_t):
            self.rotate_left(4,4)
            
        if(key==pygame.K_6):
            self.rotate_right(4,7)
        if(key==pygame.K_y):
            self.rotate_left(4,7)
            
        if(key==pygame.K_7):
            self.rotate_right(7,1)
        if(key==pygame.K_u):
            self.rotate_left(7,1)
            
        if(key==pygame.K_8):
            self.rotate_right(7,4)
        if(key==pygame.K_i):
            self.rotate_left(7,4)
            
        if(key==pygame.K_9):
            self.rotate_right(7,7)
        if(key==pygame.K_o):
            self.rotate_left(7,7)
            
    def rotate_right(self, x ,y):
        for _ in xrange(0,2):
            self.move_one(x, y)    
    
    def rotate_left(self, x ,y):
        for _ in xrange(0,6):
            self.move_one(x, y)    
    
    def move_one(self, x, y):
        tmp = self.board[x-1][y-1].color
        self.board[x-1][y-1].color = self.board[x][y-1].color
        self.board[x][y-1].color = self.board[x+1][y-1].color
        self.board[x+1][y-1].color = self.board[x+1][y].color
        self.board[x+1][y].color = self.board[x+1][y+1].color
        self.board[x+1][y+1].color = self.board[x][y+1].color
        self.board[x][y+1].color = self.board[x-1][y+1].color
        self.board[x-1][y+1].color = self.board[x-1][y].color
        self.board[x-1][y].color = tmp

    
    
        