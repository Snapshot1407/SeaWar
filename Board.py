import Exceptions
from Dot import Dot
class Board:
    def __init__(self, hide = False, size = 6):
        self.size = size
        self.hide = hide
        self.count = 0
        self.the_game_board = [["О"] * size for i in range(size)]
        self.busy = []
        self.ships = []
        self.n = 0

    @staticmethod
    def print_board(first_player, second_player):
        string = "  |"
        for i in range(len(first_player.the_game_board)):
            string += f" {i + 1} |"
        num_space = len(string)
        num_string = 1
        string += " " * (num_space-1) + string
        for i, j in zip(first_player.the_game_board, second_player.the_game_board):
            string += "\n" + "-" * num_space + " " * (num_space) + "-" * num_space
            s = str(num_string) + " | " + " | ".join(str(s) for s in j) + " |"
            if second_player.hide:
                s = s.replace("■", "0")
            string += "\n" + str(num_string) + " | " + " | ".join(str(s) for s in i) + " |" + " " * (num_space) + s
            num_string += 1

        string += "\n"
        print(string)

    def out(self, dot):
        return not(0 <= dot.x < self.size and 0 <= dot.y < self.size)
    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise Exceptions.BoardOutException()
        for dot in ship.dots:
            self.the_game_board[dot.x][dot.y] = "■"
            self.busy.append(dot)
        self.ships.append(ship)
        self.contour(ship)
    def contour(self, ship, verb = False):
        near = [
            (-1, -1), (-1, 0) , (-1, 1),
            (0, -1), (0, 0) , (0 , 1),
            (1, -1), (1, 0) , (1, 1)
        ]
        for dot in ship.dots:
            for dot_x, dot_y in near:
                cur = Dot(dot.x + dot_x, dot.y + dot_y)
                if not(self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.the_game_board[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def shot(self, dot):
        if self.out(dot):
            raise Exceptions.BoardOutException()

        if dot in self.busy:
            raise Exceptions.BoardUsedException()

        self.busy.append(dot)

        for ship in self.ships:
            if dot in ship.dots:
                ship.hitpoint -= 1
                self.the_game_board[dot.x][dot.y] = "X"
                if ship.hitpoint == 0:
                    self.count += 1
                    self.contour(ship,True)
                    print("Корабль уничтожен!")
                    return True
                else:
                    print("Корабль ранен!")
                    return True

        self.the_game_board[dot.x][dot.y] = "."
        print("Мимо!")
        return False
    def begin(self):
        self.busy = []