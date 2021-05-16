import time
import turtle
import os

from time import sleep
from constants import *
from random import *


"""Code variables"""
screen = turtle.Screen()
hud = turtle.Turtle()
pen = turtle.Turtle()
border = turtle.Turtle(visible=False)
paddle_1 = turtle.Turtle()
paddle_2 = turtle.Turtle()
ball = turtle.Turtle()


def game_hud():
    """Shows the game's display"""
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(0, 260)
    hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


def window():
    """Create the game's window"""
    screen.title("My Pong")
    screen.bgcolor('#000000')
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.tracer(0)


def set_pen(pen):
    """Set the pen"""
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


def set_paddle(paddle, xcor, ycor):
    """Creates the paddles of the game"""
    paddle.speed('fastest')
    paddle.shape("square")
    paddle.color("#000080")
    paddle.shapesize(STRETCH_WID, STRETCH_LEN)
    paddle.penup()
    paddle.goto(xcor, ycor)


def draw_border():
    """Creates the border of the game"""
    border.pensize(3)
    border.penup()
    border.setposition(-SCREEN_WIDTH, SCREEN_HEIGHT)
    border.pendown()
    border.forward(SCREEN_WIDTH)
    border.penup()
    border.sety(-SCREEN_HEIGHT / 2.5)
    border.pendown()
    border.backward(SCREEN_WIDTH)
    border.color('white')
    border.speed('fastest')


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
    ball.speed('fastest')
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1
    ball.dy = 1


def write_hud_score(score_1, score_2):
    """Write the score of the players in the hud"""
    msg = f"{score_1} : {score_2}"
    font = ("Press Start 2P", 24, "normal")
    hud.write(msg, align="center", font=font)


def update_score(score_1, score_2):
    """Update score from players"""
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        write_hud_score(score_1, score_2)
        os.system("258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1
        return score_1

    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        write_hud_score(score_1, score_2)
        os.system("258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1
        return score_2


def limit_score(score, player):
    """Sets the score limit"""
    if score == 10:
        hud.clear()
        msg_1 = f"{player} WINNER"
        msg_2 = "Click to close game"
        font_1 = ("Press Start 2P", 24, "normal")
        font_2 = ("Press Start 2P", 15, "normal")
        hud.write(msg_1, align="center", font=font_1)
        os.system("258020__kodack__arcade-bleep-sound.wav&")
        sleep(3)
        hud.clear()
        hud.write(msg_2, align="center", font=font_2)
        screen.exitonclick()


def move_ball():
    """Move the ball"""
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


def collision_ball_with_wall(score_1, score_2):
    """Responsible for the ball's collision"""
    # collision with the upper wall
    if ball.ycor() > 290:
        os.system("afplay bounce.wav&")
        ball.sety(290)
        ball.dy *= -1

    # collision with lower wall
    if ball.ycor() < -290:
        os.system("afplay bounce.wav&")
        ball.sety(-290)
        ball.dy *= -1

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
    """Responsible for the paddle's collision with the ball"""
    # collision with the paddle 1
    if ball.xcor() == paddle_1.xcor() + 20 and \
            paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50 and \
            not ball.xcor() < paddle_1.xcor():
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    # collision with the paddle 2
    if ball.xcor() == paddle_2.xcor() - 20 and \
            paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50 and \
            not ball.xcor() > paddle_2.xcor():
        ball.dx *= -1
        os.system("afplay bounce.wav&")


def main():
    """Main function of the game"""
    score_1 = 0
    score_2 = 0
    window()
    controls()
    game_hud()
    set_pen(pen)
    draw_border()
    set_paddle(paddle_1, -350, 0)
    set_paddle(paddle_2, 350, 0)
    game_ball()
    while True:

        # Define pen
        pen.goto(0, -SCREEN_HEIGHT//3)
        pen.pendown()
        pen.goto(0, SCREEN_HEIGHT//3)

        screen.update()

        # ball movement
        move_ball()

        # collision wall
        score_1, score_2 = collision_ball_with_wall(score_1, score_2)

        set_collision_paddle()


if __name__ == '__main__':
    main()
