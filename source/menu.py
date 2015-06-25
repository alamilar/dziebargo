#coding=utf-8
from Tkinter import *
from source.game import Game

class Menu:
    def __init__(self,):
        root = Tk()
        self.frame = Frame(root)
        self.frame.pack()
        self.newgame1 = Button(self.frame, text='Nowa gra dla 1 gracza', command=lambda: Game(1))
        self.newgame1.pack()
        self.newgame2 = Button(self.frame, text='Nowa gra dla 2 graczy')
        self.newgame2.pack()
        self.newgame3 = Button(self.frame, text='Nowa gra dla 3 graczy')
        self.newgame3.pack()
        self.newgame4 = Button(self.frame, text='Nowa gra dla 4 graczy')
        self.newgame4.pack()
        self.exit = Button(self.frame, text='Wyjdź', command='self.root.destroy')
        self.exit.pack()
        self.display_menu()
        root.mainloop()

    def display_menu(self):
        pass


    def game1(self):
        self.game = Game(1)
        self.game.main_loop()

    def game2(self):
        self.game = Game(2)
        self.game.main_loop()

    def game3(self):
        self.game = Game(3)
        self.game.main_loop()

    def game4(self):
        self.game = Game(4)
        self.game.main_loop()

    def quit(self):
        pass