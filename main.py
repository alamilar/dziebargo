from source.game import Game
from source.loger import log
import os
import source.constants as constants

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(constants.text_menu)
        input = raw_input()
        if input not in ('1', '2', '3', 'q'):
            continue
        if input == 'q':
            break
        game = Game(int(input))
        print game.main_loop()


if __name__ == '__main__':
    log("============================= NEW RUNME")
    if constants.debug:
        game = Game(1)
        game.main_loop()
    else:
        main()