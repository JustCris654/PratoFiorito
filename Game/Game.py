from Cell import *
from datetime import datetime, timedelta
from pathlib import Path
from SetupGame import UiDialog, start_ui
from Label import LabelDialog, label_win, label_lose

# Set the seed of the random
seed(datetime.now())

path = Path(Path(__file__).parent.parent, 'Resources')



class PratoFiorito(arcade.Window):
    def __init__(self, level):
        self.level = level
        self.scaling = 1 if self.level == 2 else 2 if self.level == 1 else 0.67

        # Set how many rows and columns we will have
        self.row_count = 5 * self.level
        self.column_count = 5 * self.level

        # This sets the WIDTH and HEIGHT of each grid location
        self.cell_width = int(48 * self.scaling)
        self.cell_height = int(50 * self.scaling)

        # This sets the margin between each cell
        # and on the edges of the screen.
        self.margin = 2 * self.scaling

        # Do the math to figure out our screen dimensions
        self.screen_width: int = int((self.cell_width + self.margin) * self.column_count + self.margin)
        self.screen_height: int = int((self.cell_height + self.margin) * self.row_count + self.margin)
        self.screen_title: str = "Prato fiorito"
        # Start the app
        super().__init__(self.screen_width, self.screen_height, self.screen_title)

        # Create a 2 dim array for store the grid
        self.grid = []  # 0 == undiscovered, 1 == discovered, 3 == undiscovered bomb, 4 == discovered bomb -> game ends
        # Set the background color
        arcade.set_background_color(arcade.color.ANTIQUE_WHITE)
        # Sprite list for the grid
        self.grid_sprite_list = None
        # The grid
        self.Grid: Grid = None

    def setup(self):
        # Conta le bombe adiacenti per tutte le caselle
        # Create the object grid
        self.Grid = Grid(self.column_count, self.row_count)
        # Call the generate_bombs function to generate randomly the bombs
        self.Grid.generate_bombs(self.level)
        # Conta le bombe adiacenti per tutte le caselle
        for i in range(self.column_count):
            for k in range(self.row_count):
                self.Grid.count_neighbours(i, k)

        self.grid_sprite_list = arcade.SpriteList()

        # Create a list of sprites to represent each grid location
        for column in range(self.column_count):
            for row in range(self.row_count):
                x = row * (self.cell_width + self.margin) + (self.cell_width / 2 + self.margin)
                y = column * (self.cell_height + self.margin) + (self.cell_height / 2 + self.margin)
                sprite = arcade.Sprite(Path(path, 'sprite_9.png'), self.scaling)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)

    def resync_grid_with_sprites(self):
        # self.shape_list = arcade.ShapeElementList()
        for row in range(self.row_count):
            for column in range(self.column_count):
                # In questa parte lavoro monodimensionalmente quindi devo convertire la grid bidimensionale in
                # monodimensionale, per esempio righa 3 e colonna 7 sarà mappata su 37
                pos = row * self.column_count + column
                if self.Grid.grid[column][row].revealed is False:
                    if self.Grid.grid[column][row].marked:
                        self.grid_sprite_list[pos].texture = arcade.load_texture(
                            Path(path, 'sprite_13.png')
                        )
                    elif self.Grid.grid[column][row].unsure:
                        self.grid_sprite_list[pos].texture = arcade.load_texture(
                            Path(path, 'sprite_12.png')
                        )
                    else:
                        self.grid_sprite_list[pos].texture = arcade.load_texture(
                            Path(path, 'sprite_9.png')
                        )
                elif self.Grid.grid[column][row].revealed is True:
                    if self.Grid.grid[column][row].is_bomb is True:
                        self.grid_sprite_list[pos].texture = arcade.load_texture(
                            Path(path, 'sprite_11.png')
                        )
                    else:
                        num = 10 if self.Grid.grid[column][row].neighboring_bombs == 0 \
                            else self.Grid.grid[column][row].neighboring_bombs
                        self.grid_sprite_list[pos].texture = arcade.load_texture(
                            Path(path, f'sprite_{num}.png')
                        )

    def on_draw(self):
        # This command has to happen before we start drawing
        arcade.start_render()
        self.grid_sprite_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (self.cell_width + self.margin))
        row = int(y // (self.cell_height + self.margin))
        print(button)

        print(
            f'Click coordinates: ({x}, {y}). '
            f'Grid coordinates: ({column}, {row}). '
            f'Grid value: {self.Grid.grid[row][column].is_bomb}'
        )

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if column < self.column_count and row < self.row_count:
            if button == arcade.MOUSE_BUTTON_LEFT:
                if self.Grid.reveal_cell(column, row) is False:
                    self.game_over()
            elif button == arcade.MOUSE_BUTTON_RIGHT:
                self.Grid.grid[column][row].unsure = False
                self.Grid.grid[column][row].marked = not self.Grid.grid[column][row].marked
            elif button == arcade.MOUSE_BUTTON_MIDDLE:
                self.Grid.grid[column][row].marked = False
                self.Grid.grid[column][row].unsure = not self.Grid.grid[column][row].unsure

        self.resync_grid_with_sprites()

    def game_over(self):
        self.Grid.reveal_all()


def main():
    level = start_ui()
    game_window = PratoFiorito(level)
    game_window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
