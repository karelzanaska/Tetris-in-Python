import copy
import time

from pyglet.window import key

from src.game import resources
from src.game.piece import Piece
from src.game.pixel import Pixel


class Game:

    def __init__(self, speed="standard"):
        self._columns = resources.COLUMNS_COUNT
        self._rows = resources.ROWS_COUNT
        self._play_window_height = resources.PLAY_WINDOW_HEIGHT
        self._play_window_width = resources.PLAY_WINDOW_WIDTH
        self._block_size = resources.BLOCK_SIZE
        self._block_border = resources.BLOCK_BORDER
        self._background_color = resources.COLORS.get("BACKGROUND")
        self._speed = resources.SPEEDS.get(speed)
        self._grid = []
        self._score = 0
        self._done = False
        self._piece = Piece(3, 0)
        self._last_time = time.time()

        self.key_handler = key.KeyStateHandler()
        self._actions = {
            key.UP: self._rotate,
            key.DOWN: self._down,
            key.LEFT: self._left,
            key.RIGHT: self._right
        }

        self._create_grid()
        self.draw()

    def _create_grid(self):
        for y in range(self._rows):
            row = []
            for x in range(self._columns):
                pixel = Pixel(self._block_size, self._block_border, self._play_window_height,
                              self._background_color, resources.ALPHA)
                row.append(pixel)
            self._grid.append(row)

    def _create_new_piece(self):
        self._piece = Piece(self._columns // 2 - 2, 0)

    def _down(self):
        self._piece.y += 1
        if self._check_cross():
            self._piece.y -= 1
            self._lock()

    def _left(self):
        old_x = self._piece.x
        self._piece.x -= 1
        if self._check_cross():
            self._piece.x = old_x

    def _right(self):
        old_x = self._piece.x
        self._piece.x += 1
        if self._check_cross():
            self._piece.x = old_x

    def _rotate(self):
        old_rotation = self._piece.rotation
        self._piece.rotate()
        if self._check_cross():
            self._piece.rotation = old_rotation

    def _check_cross(self):
        for y in range(4):
            for x in range(4):
                if 4 * y + x in self._piece.shape:
                    if y + self._piece.y > self._rows - 1 or \
                            x + self._piece.x > self._columns - 1 or \
                            x + self._piece.x < 0 or \
                            self._grid[y + self._piece.y][x + self._piece.x].locked:
                        return True
        return False

    def _lock(self):
        for y in range(4):
            for x in range(4):
                if 4 * y + x in self._piece.shape:
                    self._grid[y + self._piece.y][x + self._piece.x].locked = True
                    self._grid[y + self._piece.y][x + self._piece.x].color = self._piece.color
        self._cut_rows()
        self._create_new_piece()
        if self._check_cross():
            self._done = True

    def _cut_rows(self):
        for y in range(1, self._rows):
            locked_pixels = 0
            for x in range(self._columns):
                if self._grid[y][x].locked:
                    locked_pixels += 1
                if locked_pixels == self._columns:
                    self._score += 1
                    for k in range(y, 1, -1):
                        for x in range(self._columns):
                            new_piece = copy.copy(self._grid[k-1][x])
                            self._grid[k][x] = new_piece

    def update(self):
        current_time = time.time()
        if current_time - self._last_time > self._speed - (self._score / 100):
            self._last_time = current_time
            self._down()

        for pressed_key, value in self.key_handler.items():
            if value and pressed_key in self._actions.keys():
                self._actions[pressed_key]()

    def draw(self):
        for y, row in enumerate(self._grid):
            for x, pixel in enumerate(row):
                if not pixel.locked:
                    pixel.color = self._background_color
                pixel.draw(x, y + 1)

        if self._piece is not None:
            for i in range(4):
                for j in range(4):
                    if (4 * i + j) in self._piece.shape:
                        pixel = self._grid[i + self._piece.y][j + self._piece.x]
                        pixel.color = self._piece.color
                        pixel.draw(j + self._piece.x, i + self._piece.y + 1)
        return self._done, self._score
