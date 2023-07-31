from random import randint
from Board import Board
from Dot import Dot
import Exceptions
from Ship import Ship
from Player import AI, User


class Game():
    def __init__(self, size = 10):
        self.size = size
        self.player = self.random_board()
        self.comp = self.random_board()
        self.comp.hide = True
        self.player.hide = False

        self.ai = AI(self.comp, self.player)
        self.user = User(self.player,self.comp)

    def try_board(self):
        lens = [4,3,3,2, 2, 2, 1, 1, 1, 1]
        board = Board(size = self.size, hide= True)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except Exceptions.BoardException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def loop(self):
        num = 0
        while True:
            Board.print_board(self.user.my_board, self.ai.my_board)
            if num % 2 == 0:
                print("Ходит пользователь!")
                repeat = self.user.move()
            else:
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.my_board.count == 7:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.user.my_board.count == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

if __name__ == '__main__':
    game = Game()
    game.start()