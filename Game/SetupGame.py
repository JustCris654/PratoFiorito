# Set the level to play and the scaling of the sprites
LEVEL: int = 1
SCALING = 1 if LEVEL == 2 else 2 if LEVEL == 1 else 0.67

# Set how many rows and columns we will have
ROW_COUNT = 5 * LEVEL
COLUMN_COUNT = 5 * LEVEL

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 48 * SCALING
HEIGHT = 50 * SCALING

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 2 * SCALING

# Do the math to figure out our screen dimensions
SCREEN_WIDTH: int = int((WIDTH + MARGIN) * COLUMN_COUNT + MARGIN)
SCREEN_HEIGHT: int = int((HEIGHT + MARGIN) * ROW_COUNT + MARGIN)
SCREEN_TITLE: str = "Prato fiorito"