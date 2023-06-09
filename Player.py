import random

import Exceptions
from Dot import Dot


class Player:
    def __init__(self,my_board, opponent_board):
        self.my_board = my_board
        self.opponent_board = opponent_board
        self.the_game_board = my_board.the_game_board
        self.hide = my_board.hide
    def ask(self):
        pass
    def get_size(self):
        return self.my_board.get_len_board()
    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.opponent_board.shot(target)
                return repeat
            except Exceptions.BoardException as be:
                print(be)
    def print_string(self,num):
        return self.my_board[num]
class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)
class AI(Player):
    def ask(self):
        dot = Dot(random.randint(0,5),random.randint(0,5))
        print(f"Ход компьютера: {dot.x + 1} {dot.y + 1}")
        return dot



