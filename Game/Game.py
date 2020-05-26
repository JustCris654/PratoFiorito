import arcade
from random import seed, randint
from Cell import *

# Set the level to play and the scaling of the sprites
LEVEL: int = 2
SCALING = 1 if LEVEL == 2 else 2 if LEVEL == 1 else 0.67

# Set how many rows and columns we will have
ROW_COUNT = 5 * LEVEL
COLUMN_COUNT = 5 * LEVEL

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 48 * SCALING
HEIGHT = 50 * SCALING

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5 * SCALING

# Do the math to figure out our screen dimensions
SCREEN_WIDTH: int = int((WIDTH + MARGIN) * COLUMN_COUNT + MARGIN)
SCREEN_HEIGHT: int = int((HEIGHT + MARGIN) * ROW_COUNT + MARGIN)
SCREEN_TITLE: str = "Prato fiorito"

# Set the seed of the random
seed(0)


class PratoFiorito(arcade.Window):
    def __init__(self):

        # Start the app
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Create a 2 dim array for store the grid
        self.grid = []  # 0 == undiscovered, 1 == discovered, 3 == undiscovered bomb, 4 == discovered bomb -> game ends
        # Set the background color
        arcade.set_background_color(arcade.color.ANTIQUE_WHITE)
        # Sprite list for the grid
        self.grid_sprite_list = None
        # The grid
        self.Grid = None

    def setup(self):

        # Create the object grid
        self.Grid = Grid(COLUMN_COUNT, ROW_COUNT, SCALING)
        # Call the generate_bombs function to generate randomly the bombs
        self.Grid.generate_bombs(LEVEL)

        self.grid_sprite_list = arcade.SpriteList()

        # Create a list of sprites to represent each grid location
        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT):
                x = row * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
                y = column * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
                sprite = arcade.Sprite('/home/justcris/PycharmProjects/Prato_Fiorito/Resources/sprite_9.png', SCALING)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)

    def resync_grid_with_sprites(self):
        # self.shape_list = arcade.ShapeElementList()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # In questa parte lavoro monodimensionalmente quindi devo convertire la grid bidimensionale in
                # monodimensionale, per esempio righa 3 e colonna 7 sarà mappata su 37
                pos = row * COLUMN_COUNT + column
                if self.Grid.grid[column][row].revealed is False:
                    self.grid_sprite_list[pos].texture = arcade.load_texture(
                        '/home/justcris/PycharmProjects/Prato_Fiorito/Resources/sprite_9.png'
                    )
                elif self.Grid.grid[column][row].revealed is True:
                    if self.Grid.grid[column][row].is_bomb is True:
                        self.grid_sprite_list[pos].texture = arcade.load_texture(
                            '/home/justcris/PycharmProjects/Prato_Fiorito/Resources/sprite_11.png'
                        )
                    else:
                        # Count neighbours
                        self.grid_sprite_list[pos].texture = arcade.load_texture(
                            '/home/justcris/PycharmProjects/Prato_Fiorito/Resources/sprite_10.png'
                        )

    def on_draw(self):
        # This command has to happen before we start drawing
        arcade.start_render()
        self.grid_sprite_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        print(
            f"Click coordinates: ({x}, {y}). Grid coordinates: ({column}, {row}). Grid value: {self.Grid.grid[row][column].is_bomb}")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if column < COLUMN_COUNT and row < ROW_COUNT:
            if self.Grid.grid[column][row].revealed is False:
                self.Grid.grid[column][row].revealed = True

        self.resync_grid_with_sprites()


def main():
    game_window = PratoFiorito()
    game_window.setup()
    for i in range(ROW_COUNT):
        for k in range(COLUMN_COUNT):
            print(f'{0 if game_window.Grid.grid[i][k].is_bomb else 1} | ', end='')
        print('')
    arcade.run()


if __name__ == "__main__":
    main()
