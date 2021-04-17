import argparse

import pyglet

from src.game import resources
from src.game.game import Game


ap = argparse.ArgumentParser()

ap.add_argument("-s", "--speed", required=False, help="Game speed", choices=["slow", "standard", "fast"],
                default="standard")

args = vars(ap.parse_args())

game_window = pyglet.window.Window(resources.PLAY_WINDOW_WIDTH, resources.PLAY_WINDOW_HEIGHT + 130)

game = Game(args["speed"])

game_window.push_handlers(game.key_handler)

done_label = pyglet.text.Label(text="KONEC HRY!", x=10, y=resources.PLAY_WINDOW_HEIGHT + 70, font_size=25,
                               color=(255, 255, 255, 255))
score_label = pyglet.text.Label(text="", x=10, y=resources.PLAY_WINDOW_HEIGHT + 25, font_size=25,
                                color=(255, 255, 255, 255))

done = False


def update(dt):
    global done, game
    if not done:
        game.update()


@game_window.event
def on_draw():
    game_window.clear()

    global done, game
    done, score = game.draw()
    if done:
        done_label.draw()
    score_label.text = "SCORE: {}".format(score)
    score_label.draw()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 10)
    pyglet.app.run()
