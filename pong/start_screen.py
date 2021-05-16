import os
import turtle

from turtle import Turtle, Screen

from constants import *
from play_sounds import play_sound_bounce, play_sound_bleep


screen = Screen()
title_game = Turtle()
start_button = Turtle()
level_button = Turtle()
quit_button = Turtle()    


def setup_screen():
    """Define setup screen"""
    screen.title("Start Game")
    screen.bgcolor("black")
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)


def setup_title():
    """Define setup title"""
    text_title = "Pong CDD"
    title_game.speed(3)
    title_game.hideturtle()
    title_game.penup()
    title_game.clear()
    title_game.goto(0, 170)
    title_game.color("white")
    title_game.write(text_title, align="center", font=FONT_SIZE_32)


def setup_start_button():
    """Define setup button start"""
    text_button = "Start Game"
    start_button.speed(3)
    start_button.hideturtle()
    start_button.clear()
    start_button.penup()
    start_button.goto(0, 50)
    start_button.color("green")
    start_button.shape("square")
    start_button.write(text_button, align="center", font=FONT_SIZE_26)


def setup_level_button():
    """Define setup button level"""
    text_button = "Level"
    level_button.speed(3)
    level_button.hideturtle()
    level_button.penup()
    level_button.clear()
    level_button.goto(0, 0)
    level_button.color("blue")
    level_button.shape("square")
    level_button.write(text_button, align="center", font=FONT_SIZE_26)


def setup_quit_button():
    """Define setup button quit"""
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
    """Start game"""
    play_sound_bounce()
    print('start')
    os.system("python ./pong.py&")
    screen.bye()


def level_game():
    """Level game"""
    play_sound_bounce()
    print('level')
    os.system("python ./choice_level.py")
    screen.bye()


def quit_game():
    """Quit game"""
    play_sound_bleep()
    screen.bye()


def _onclick(x, y):
    """Select button by position"""
    if (-36.0 <= x <= 43.0) and (57.0 <= y <= 85.0):
        start_game()
    elif (-36.0 <= x <= 43.0) and (-48.0 <= y <= -14.0):
        quit_game()
    elif (-36.0 <= x <= 43.0) and (2.0 <= y <= 35.0):
        level_game()
    print((x, y))


def handle_loop():
    """Check click on screen"""
    turtle.onscreenclick(_onclick)


def main():
    setup_screen()
    setup_title()
    setup_start_button()
    setup_level_button()
    setup_quit_button()
    screen.listen()
    handle_loop()
    screen.mainloop()


if __name__ == '__main__':
    main()
