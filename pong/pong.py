import turtle
import os
import time

from random import randint, choice
from time import sleep

from constants import *
from play_sounds import play_sound_bleep, play_sound_bounce
from choice_level import choice_level_func


""" Code variables"""
screen = turtle.Screen()
hud = turtle.Turtle()
pen = turtle.Turtle()
border = turtle.Turtle(visible=False)
paddle_1 = turtle.Turtle()
paddle_2 = turtle.Turtle()
ball = turtle.Turtle()


def game_hud():
    """ Shows the game's display"""
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(0, 260)
    hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


def setup_screen():
    """ Create the game's window"""
    screen.title("PONG - CDD")
    screen.bgcolor("#000000")
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.tracer(0)


def set_pen(pen):
    """ Set the pen"""
    pen.hideturtle()
    pen.penup()
    pen.color('#717D7E')
    pen.pensize(3)
    return pen


def controls():
    """Set the game's controls"""
    screen.listen()
    screen.onkeypress(paddle_1_up, "w")
    screen.onkeypress(paddle_1_down, "s")
    screen.onkeypress(paddle_2_up, "Up")
    screen.onkeypress(paddle_2_down, "Down")


def set_paddle(paddle, xcor, ycor, color="white"):
    """ Creates the paddles of the game"""
    paddle.speed(10)
    paddle.shape("square")
    paddle.color(color)
    paddle.shapesize(PLAYER_HEIGHT / CURSOR_SIZE,  
                     PLAYER_WIDTH / CURSOR_SIZE)
    paddle.penup()
    paddle.goto(xcor, ycor)


def draw_border():
    """ Creates the border of the game"""
    border.color('white')
    border.pensize(2)
    border.penup()
    border.setposition(-SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    border.pendown()
    for side in range(2):
        border.forward(SCREEN_WIDTH)
        border.penup()
        border.sety(-SCREEN_HEIGHT / 2)
        border.pendown()
        border.backward(SCREEN_WIDTH)


def move_up(paddle):
    """Move the paddles upwards"""
    y = paddle.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle.sety(y)


def paddle_1_up():
    """Move the left paddle up"""
    move_up(paddle_1)


def paddle_2_up():
    """ Move the right paddle up"""
    move_up(paddle_2)


def move_down(paddle):
    """Move the paddles downwards"""
    y = paddle.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle.sety(y)


def paddle_1_down():
    """Move the left paddle down"""
    move_down(paddle_1)


def paddle_2_down():
    """Move the left paddle down"""
    move_down(paddle_2)


def game_ball():
    """Create the game's ball"""
    ball.speed(10)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1
    ball.dy = 1


def reset_ball():
    ball.goto(0, 0)
    ball.setheading(choice([0, 180]) + randint(-60, 60))


def write_hud_score(score_1, score_2):
    """Write the score of the players in the hud"""
    msg = f"{score_1}     :     {score_2}"
    font = ("Press Start 2P", 24, "normal")
    hud.write(msg, align="center", font=font)


def update_score(score_1, score_2):
    """Update score from players"""
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        write_hud_score(score_1, score_2)
        play_sound_bleep()
        reset_ball()
        return score_1

    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        write_hud_score(score_1, score_2)
        play_sound_bleep()
        reset_ball()
        return score_2


def limit_score(score, player):
    """Sets the score limit"""
    if score == 10:
        hud.clear()
        msg_1 = f"WINNER: {player} "
        msg_2 = "Click to close game"
        font_1 = ("Press Start 2P", 24, "normal")
        font_2 = ("Press Start 2P", 15, "normal")
        hud.write(msg_1, align="center", font=font_1)
        play_sound_bleep()
        sleep(3)
        hud.clear()
        hud.write(msg_2, align="center", font=font_2)
        screen.exitonclick()


def move_ball():
    """Move the ball"""
    if level == 1:
        ball.forward(5)
    elif level == 2:
        ball.forward(7)
    elif level == 3:
        ball.forward(10)


def collision_ball_with_wall(score_1, score_2):
    """Responsible for the ball's collision"""
    # collision with the upper wall
    if ball.ycor() > 290:
        ball.setheading(-ball.heading())
        play_sound_bounce()


    # collision with lower wall
    if ball.ycor() < -290:
        ball.setheading(-ball.heading())
        play_sound_bounce()

    # collision with left wall
    if ball.xcor() < -390:
        score_2 = update_score(score_1, score_2)
        limit_score(score_2, PLAYER_2)

    # collision with right wall
    if ball.xcor() > 390:
        score_1 = update_score(score_1, score_2)
        limit_score(score_1, PLAYER_1)

    return score_1, score_2


def set_collision_paddle():
       # collision with the paddle 1
    if ball.xcor() > paddle_1.xcor() and \
            abs(ball.xcor() - paddle_1.xcor()) < 15 and \
            abs(ball.ycor() - paddle_1.ycor()) < (PLAYER_HEIGHT/2):
        ball.setheading(choice([-45, -30, -15, 0, 15, 30, 45]))
        ball.speed(8)
        play_sound_bounce()

    # collision with the paddle 2
    elif ball.xcor() < paddle_2.xcor() and \
            abs(ball.xcor() - paddle_2.xcor()) < 15 and \
            abs(ball.ycor() - paddle_2.ycor()) < (PLAYER_HEIGHT/2):
        ball.setheading(choice([-135, -150, -165, 180, 165, 150, 135]))
        ball.speed(8)
        play_sound_bounce()


def define_level_game():
    global level
    with open('level', 'r') as fl:
        level = int(fl.read())
    print(level)


def main():
    """Main function of the game"""
    define_level_game()

    score_1 = 0
    score_2 = 0
    setup_screen()
    controls()
    game_hud()
    set_pen(pen)
    draw_border()
    set_paddle(paddle_1, -350, 0, "#000080")
    set_paddle(paddle_2, 350, 0, "red")
    game_ball()
    while True:

        # Define pen
        pen.goto(0, -SCREEN_HEIGHT//3)
        pen.pendown()
        pen.goto(0, SCREEN_HEIGHT//3)

        # Update screen
        screen.update()

        # ball movement
        move_ball()

        # collision wall
        score_1, score_2 = collision_ball_with_wall(score_1, score_2)

        set_collision_paddle()
        sleep(0.01)


if __name__ == '__main__':
    main()
