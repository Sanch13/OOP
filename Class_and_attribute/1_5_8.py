from typing import List
from random import randint

class Cell:
    def __init__(self, mine: bool = False, around_mines: int = 0):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = False


class GamePole:
    def __init__(self, n: int, m: int):
        self.n = n
        self.pole = [[Cell() for _ in range(self.n)] for _ in range(self.n)]
        self.amount = m
        self.init()

    def init(self):
        m = 0
        while m < self.amount:
            i = randint(0, self.n - 1)
            j = randint(0, self.n - 1)
            if self.pole[i][j].mine:
                continue

            self.pole[i][j].mine = True
            m += 1

        cells = (-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)
        for x in range(self.n):
            for y in range(self.n):
                if not self.pole[x][y].mine:
                    mines = sum(self.pole[x + i][y + j] for i, j in cells
                                if 0 < x + i < self.n and 0 < y + j < self.n)
                    self.pole[x][y].around_mines = mines

    def show(self):
        pass


pole_game = GamePole(10, 12)
