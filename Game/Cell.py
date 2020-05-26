import arcade
from random import seed, randint

seed(0)


class Cell(object):
    def __init__(self, is_bomb, scaling, column, row):
        # True if the cell is a bomb, false otherwise
        self.is_bomb = is_bomb
        # True if the cell is revealed, false otherwise
        self.revealed = False
        # True if the cell is marked
        self.marked = False
        # Number of neighboring bombs
        self.neighboring_bombs = None

        # Variables for the rendering
        self.scaling = scaling
        self.column = column
        self.row = row


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

    def count_neighbours(self):
        pass
