from turtle import Turtle, Screen

from constants import SCREEN_WEIGHT, SCREEN_WIDTH


class TitleGame:
    def __init__(self, title_game):
        self.title_game = Turtle()
        self.title_game.speed()
        self.title_game.penup()
        self.title_game.clear()
        self.title_game.shape("square")
        self.title_game.color("white")
        self.title_game.write(title_game,
                              align="center",
                              font=("Press Start 2P", 32, "normal"))
        self.title_game.setposition(x=0, y=500)


class ButtonOnScreen:
    def __init__(self, text_button):
        self.button = Turtle()
        self.button.speed(0)
        self.button.penup()
        self.button.clear()
        self.button.shape("square",)
        self.button.color("white")
        self.button.write(text_button,
                          align="center",
                          font=("Press Start 2P", 26, "normal"))


class StartScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.title("Start Game")
        self.screen.bgcolor("black")
        self.screen.setup(SCREEN_WIDTH, SCREEN_WEIGHT)

        self.title = TitleGame("Pong with Turtle")

        self.start_button = ButtonOnScreen("Start")
        self.quit_button = ButtonOnScreen("Quit")

    def listening_screen(self):
        """Listening screen method is on infinity loop, in that all actions of
        buttons are calls
        """
        while True:
            self.screen.update()


def main():
    a = StartScreen()
    a.listening_screen()

    # while True:


if __name__ == '__main__':
    main()
