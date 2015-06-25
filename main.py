from source.game import Game
from source.loger import log
import os
import source.constants as constants


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(constants.TEXT_MENU)
        user_input = raw_input()
        if user_input not in ('1', '2', '3', 'q'):
            continue
        if user_input == 'q':
            break
        game = Game(int(user_input))
        print game.main_loop()


if __name__ == '__main__':
    log("============================= NEW RUNME")
    main()