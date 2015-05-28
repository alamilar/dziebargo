from source.game import Game
from loger import log
import os
import constants

def main():
    while True:
        os.system('cls')
        print(constants.text_menu)
        input = raw_input()
        if input not in ('1', '2', '3', '4', 'q'):
            continue
        if input == 'q':
            break
        game = Game(int(input))
        game.main_loop()


if __name__ == '__main__':
    log("============================= NEW RUNME")
    if constants.debug:
        game = Game(3)
        game.main_loop()
    else:
        main()