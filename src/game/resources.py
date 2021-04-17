WINDOW_WIDTH = 800
WINDOW_HEIGHT = 750
BLOCK_SIZE = 30
BLOCK_BORDER = 6
COLUMNS_COUNT = 10
ROWS_COUNT = 20
PLAY_WINDOW_WIDTH = BLOCK_SIZE * COLUMNS_COUNT
PLAY_WINDOW_HEIGHT = BLOCK_SIZE * ROWS_COUNT

TOP_LEFT_X = (WINDOW_WIDTH - PLAY_WINDOW_WIDTH) // 2
TOP_LEFT_Y = (WINDOW_HEIGHT - PLAY_WINDOW_HEIGHT) - 50

ALPHA = (200, 255)

COLORS = {
    "BLACK": (0, 0, 0),
    "GREEN": (0, 255, 0),
    "RED": (255, 0, 0),
    "BLUE": (0, 255, 255),
    "BLUE": (0, 0, 255),
    "PURPLE": (128, 0, 128),
    "YELLOW": (255, 255, 0),
    "ORANGE": (255, 165, 0),
    "PINK": (255, 50, 255),
    "BACKGROUND": (255, 255, 255)
}

SPEEDS = {
    "slow": 3 / 2,
    "standard": 2 / 3,
    "fast": 2 / 5
}

SHAPES = {
    "S": {
        "format": [[6, 7, 9, 10], [1, 5, 6, 10]],
        "color": COLORS["GREEN"]
    },
    "Z": {
        "format": [[4, 5, 9, 10], [2, 6, 5, 9]],
        "color": COLORS["RED"]
    },
    "I": {
        "format": [[1, 5, 9, 13], [4, 5, 6, 7]],
        "color": COLORS["BLUE"]
    },
    "O": {
        "format": [[1, 2, 5, 6]],
        "color": COLORS["PURPLE"]
    },
    "J": {
        "format": [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        "color": COLORS["YELLOW"]
    },
    "L": {
        "format": [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        "color": COLORS["ORANGE"]
    },
    "T": {
        "format": [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        "color": COLORS["PINK"]
    }
}
