from Cell import randint, seed, Cell, Grid, LEVEL, SCALING, ROW_COUNT, COLUMN_COUNT, WIDTH, HEIGHT, \
    MARGIN, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, arcade
from datetime import datetime
from pathlib import Path

# Set the seed of the random
seed(datetime.now())

path = Path(Path(__file__).parent.parent, 'Resources')


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
        self.Grid: Grid = None

    def setup(self):

        # Create the object grid
        self.Grid = Grid(COLUMN_COUNT, ROW_COUNT, SCALING)
        # Call the generate_bombs function to generate randomly the bombs
        self.Grid.generate_bombs(LEVEL)
        # Conta le bombe adiacenti per tutte le caselle
        for i in range(COLUMN_COUNT):
            for k in range(ROW_COUNT):
                self.Grid.count_neighbours(i, k)

        self.grid_sprite_list = arcade.SpriteList()

        # Create a list of sprites to represent each grid location
        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT):
                x = row * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
                y = column * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
                sprite = arcade.Sprite(Path(path, 'sprite_9.png'), SCALING)
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
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))
        print(button)

        print(
            f'Click coordinates: ({x}, {y}). '
            f'Grid coordinates: ({column}, {row}). '
            f'Grid value: {self.Grid.grid[row][column].is_bomb}'
        )

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if column < COLUMN_COUNT and row < ROW_COUNT:
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
    game_window = PratoFiorito()
    game_window.setup()
    for i in range(ROW_COUNT):
        for k in range(COLUMN_COUNT):
            print(f'{0 if game_window.Grid.grid[i][k].is_bomb else 1} | ', end='')
        print('')
    arcade.run()


if __name__ == "__main__":
    main()
