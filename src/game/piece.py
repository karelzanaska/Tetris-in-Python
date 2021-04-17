import random

from pyglet.window import key

from src.game import resources


class Piece:

    def __init__(self, x, y):
        self.piece_key = random.choice(list(resources.SHAPES.keys()))
        self._shape = resources.SHAPES.get(self.piece_key).get("format")
        self._color = resources.SHAPES.get(self.piece_key).get("color")
        self.x = x
        self.y = y
        self.rotation = 0
        self.locked = False

    @property
    def shape(self):
        return self._shape[self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self._shape)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not isinstance(color, tuple) or len(color) != 3:
            raise TypeError("Color must be type of tuple with length of 3.")
        for value in color:
            if value < 0 or value > 255:
                raise ValueError("Each component of the color must be in the range of 0-255")
        if color != self.color:
            self._color = color
