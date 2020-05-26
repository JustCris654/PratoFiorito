import arcade
from random import seed, randint
from SetupGame import *

seed(0)


class Cell(object):
    def __init__(self, is_bomb, scaling, column, row):
        # True if the cell is a bomb, false otherwise
        self.is_bomb = is_bomb
        # True if the cell is revealed, false otherwise
        self.revealed = False
        # Number of neighboring bombs
        self.neighboring_bombs = None
        # Unsure
        self.unsure = False
        # True if the cell is marked
        self.marked = False


class Grid(object):
    def __init__(self, column_count, row_count, scaling):
        self.grid_sprite_list = arcade.SpriteList()
        self.row_count = row_count
        self.column_count = column_count
        self.grid = [[Cell(False, scaling, row, column) for row in range(self.row_count)]
                     for column in range(self.column_count)]

    def generate_bombs(self, level):
        max_bombs = level * 5
        print(max_bombs)
        i = 0
        while i < max_bombs:
            column_bomb = randint(0, self.row_count - 1)
            row_bomb = randint(0, self.column_count - 1)
            if self.grid[column_bomb][row_bomb].is_bomb is False:
                self.grid[column_bomb][row_bomb].is_bomb = True
                i += 1

    def reveal_cell(self, column, row):
        self.grid[column][row].revealed = True

        if self.grid[column][row].is_bomb:
            return False

        if self.grid[column][row].neighboring_bombs == 0:

            pos_x = column - 1
            pos_y = row
            if 0 <= pos_x < COLUMN_COUNT and 0 <= pos_y < ROW_COUNT:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            pos_x = column + 1
            pos_y = row
            if 0 <= pos_x < COLUMN_COUNT and 0 <= pos_y < ROW_COUNT:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            pos_x = column
            pos_y = row - 1
            if 0 <= pos_x < COLUMN_COUNT and 0 <= pos_y < ROW_COUNT:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            pos_x = column
            pos_y = row + 1
            if 0 <= pos_x < COLUMN_COUNT and 0 <= pos_y < ROW_COUNT:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            pos_x = column - 1
            pos_y = row + 1
            if 0 <= pos_x < COLUMN_COUNT and 0 <= pos_y < ROW_COUNT:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            pos_x = column - 1
            pos_y = row - 1
            if 0 <= pos_x < COLUMN_COUNT and 0 <= pos_y < ROW_COUNT:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            pos_x = column + 1
            pos_y = row - 1
            if 0 <= pos_x < COLUMN_COUNT and 0 <= pos_y < ROW_COUNT:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            pos_x = column + 1
            pos_y = row + 1
            if 0 <= pos_x < COLUMN_COUNT and 0 <= pos_y < ROW_COUNT:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

    def count_neighbours(self, column, row):
        # Se la cella stessa è una bomba restituisco falso
        if self.grid[column][row].is_bomb is True:
            return None

        # Conto le bombe adiacenti alla casella
        total = 0
        for i in range(-1, 2):
            for k in range(-1, 2):
                pos_x = column + i
                pos_y = row + k
                if 0 <= pos_x < COLUMN_COUNT and 0 <= pos_y < ROW_COUNT:
                    if self.grid[pos_x][pos_y].is_bomb is True:
                        total += 1

        # Assegno il valore di bombe adiacenti al parametro
        self.grid[column][row].neighboring_bombs = total

    def reveal_all(self):
        for i in self.grid:
            for k in i:
                k.revealed = True
