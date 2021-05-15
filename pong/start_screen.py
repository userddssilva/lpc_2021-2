import os
import simpleaudio as sa

from turtle import Turtle, Screen

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class TitleGame:
    def __init__(self):
        self.title_game = Turtle()
        self.title_game.speed()
        self.title_game.penup()
        self.title_game.clear()
        self.title_game.color("white")
        self.title_game.hideturtle()
        self.font = ("Press Start 2P", 32, "normal")

    def set_text(self, title):
        self.title_game.write(title, align="center", font=self.font)

    def set_position(self, x=0, y=200):
        self.title_game.goto(x=x, y=y)


class ButtonOnScreen:
    def __init__(self):
        self.button = Turtle()
        self.button.speed(0)
        self.button.penup()
        self.button.clear()
        self.button.shape("square",)
        self.button.color("white")
        self.button.hideturtle()
        self.font = ("Press Start 2P", 26, "normal")

    def set_text(self, text_button):
        self.button.write(text_button, align="center", font=self.font)

    def set_position(self, x=0, y=200):
        self.button.goto(x=x, y=y)


class StartScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.title("Start Game")
        self.screen.bgcolor("black")
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.title = TitleGame()
        self.start_button = ButtonOnScreen()
        self.quit_button = ButtonOnScreen()

    def main_function_screen(self):
        """Listening screen method is on infinity loop, in that all actions of
        buttons are calls
        """
        self.title.set_position()
        self.title.set_text("Pong with Turtle")

        self.start_button.set_position(x=0, y=50)
        self.start_button.set_text("Start")

        self.quit_button.set_position(x=0, y=-30)
        self.quit_button.set_text("Quit")

        # path_sound = os.path.join('sounds', 'synthware_loop_sound.wav')
        # wave_obj = sa.WaveObject.from_wave_file(path_sound)
        # play_obj = wave_obj.play()
        # play_obj.wait_done()

        # play_obj = sa.play_buffer(path_sound, 2, 2, 44100)

        while True:
            self.screen.update()


def main():
    a = StartScreen()
    a.main_function_screen()


if __name__ == '__main__':
    main()
