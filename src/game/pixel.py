import pyglet


class Pixel:

    def __init__(self, size, border, window_height, color, alpha):
        self._size = size
        self._border = border
        self._window_height = window_height
        self._color = color
        self._alpha = alpha
        self.locked = False

        self._background = pyglet.image.SolidColorImagePattern((self._color[0], self._color[1], self._color[2],
                                                                self._alpha[0])) \
            .create_image(self._size, self._size)

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
            self._background = pyglet.image.SolidColorImagePattern(
                (self._color[0], self._color[1], self._color[2], self._alpha[0])) \
                .create_image(self._size, self._size)

    def draw(self, x, y):
        self._background.blit(x * self._size, self._window_height - y * self._size)
