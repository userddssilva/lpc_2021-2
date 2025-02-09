import os
from time import sleep
from turtle import Turtle, Screen
import turtle

from constants import FONT_SIZE_26, SCREEN_WIDTH, SCREEN_HEIGHT

global level


def write_level():
    """Define write text"""
    _hud = turtle.Turtle(visible=False)
    _text = 'Choose a level:'
    _hud.goto(-260, 150)
    _hud.color('#717D7E')
    _hud.write(_text, align="left", font=FONT_SIZE_26)


def setup_level_3():
    """Define setup level  3"""
    level_3 = Turtle()
    level_3.speed(3)
    level_3.hideturtle()
    level_3.clear()
    level_3.penup()
    level_3.goto(0, -70)
    level_3.shape("square")
    level_3.color("blue")
    level_3.write("Level 3", align="center", font=FONT_SIZE_26)


def setup_level_2():
    """Define setup level  2"""
    level_2 = Turtle()
    level_2.speed(3)
    level_2.hideturtle()
    level_2.clear()
    level_2.penup()
    level_2.goto(0, 0)
    level_2.shape("square")
    level_2.color("green")
    level_2.write("Level 2", align="center", font=FONT_SIZE_26)


def setup_level_1():
    """Define setup level  1"""
    level_1 = Turtle()
    level_1.speed(3)
    level_1.hideturtle()
    level_1.clear()
    level_1.penup()
    level_1.goto(0, 70)
    level_1.color("white")
    level_1.shape("square")
    level_1.write("Level 1", align="center", font=FONT_SIZE_26)


# noinspection SpellCheckingInspection
def set_level(set_l):
    global level
    level = set_l
    with open('level', 'w') as fl:
        fl.write(str(level))
    # _screen.bye()
    os.system("python ./start_screen.py&")


def _onclick(x, y):
    """Select level by position"""
    print((x, y))
    if (-60.0 <= x <= 99.0) and (72.0 <= y <= 114.0):
        set_level(1)
        print('Level 1')

    elif (-60.0 <= x <= 99.0) and (3.0 <= y <= 43.0):
        set_level(2)
        # _screen.bye()
        # os.system("python ./start_screen.py&")

    elif (-60.0 <= x <= 99.0) and (-70 <= y <= -28):
        set_level(3)
        # _screen.bye()
        # os.system("python ./start_screen.py&")


# noinspection PyGlobalUndefined
def choice_level_func():
    """choice fasted ball level"""
    global _screen
    _screen = Screen()
    _screen.bgcolor("black")
    _screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    write_level()
    setup_level_1()
    setup_level_2()
    setup_level_3()
    turtle.onscreenclick(_onclick)
    _screen.mainloop()
    _screen.bye()


def main():
    choice_level_func()


if __name__ == "__main__":
    main()
