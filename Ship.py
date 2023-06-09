from Dot import Dot
from random import randint
class Ship:
    def __init__(self, dot, len , orientation):
        self.dot = dot
        self.len = len
        self.orientation = orientation
        self.hitpoint = len
    @property
    def dots(self):
        ship_dots = []
        for i in range(self.len):
            x = self.dot.x
            y = self.dot.y
            if self.orientation == 1:
                y += i
            else:
                x += i
            ship_dots.append(Dot(x,y))
        return ship_dots

    def shooten(self, shot):
        return shot in self.dots
