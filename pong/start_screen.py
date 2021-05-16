import os
import turtle

from turtle import Turtle, Screen

from constants import *
from play_sounds import play_sound_bounce, play_sound_bleep


screen = Screen()
title_game = Turtle()
start_button = Turtle()
quit_button = Turtle()


def setup_screen():
    screen.title("Start Game")
    screen.bgcolor("black")
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)


def setup_title():
    text_title = "Pong with game"
    title_game.speed(3)
    title_game.hideturtle()
    title_game.penup()
    title_game.clear()
    title_game.goto(0, 170)
    title_game.color("blue")
    title_game.write(text_title, align="center", font=FONT_SIZE_32)


def setup_start_button():
    text_button = "Start"
    start_button.speed(3)
    start_button.hideturtle()
    start_button.clear()
    start_button.penup()
    start_button.goto(0, 50)
    start_button.color("green")
    start_button.shape("square")
    start_button.write(text_button, align="center", font=FONT_SIZE_26)


def setup_quit_button():
    text_button = "Quit"
    quit_button.speed(3)
    quit_button.hideturtle()
    quit_button.penup()
    quit_button.clear()
    quit_button.goto(0, -50)
    quit_button.color("red")
    quit_button.shape("square")
    quit_button.write(text_button, align="center", font=FONT_SIZE_26)


def start_game():
    play_sound_bleep()
    print('start')
    os.system("python ./pong.py&")
    screen.bye()


def quit_game():
    play_sound_bounce()
    screen.bye()


def _onclick(x, y):
    if (-36.0 <= x <= 43.0) and (57.0 <= y <= 85.0):
        start_game()
    elif (-36.0 <= x <= 43.0) and (-48.0 <= y <= -14.0):
        quit_game()
    print((x, y))


def handle_loop():
    turtle.onscreenclick(_onclick)


def main():
    setup_screen()
    setup_title()
    setup_start_button()
    setup_quit_button()
    screen.listen()
    handle_loop()
    screen.mainloop()


if __name__ == '__main__':
    main()
