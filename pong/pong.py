import turtle
import os

from constants import *


screen = turtle.Screen()
hud = turtle.Turtle()
paddle_1 = turtle.Turtle()
paddle_2 = turtle.Turtle()
ball = turtle.Turtle()


def game_hud():
    """ Game display"""
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(0, 260)
    hud.write("0:0", align="center", font=("Press Start 2P", 24, "normal"))


def set_screen():
    """Set config screen"""
    screen.title("My Pong")
    screen.bgcolor("black")
    screen.setup(SCREEN_WIDTH, SCREEN_WEIGHT)
    screen.tracer()


def listen_keyboard():
    """This function listen the keys press used in game"""
    screen.listen()
    screen.onkeypress(paddle_1_up, "w")
    screen.onkeypress(paddle_1_down, "s")
    screen.onkeypress(paddle_2_up, "Up")
    screen.onkeypress(paddle_2_down, "Down")


def set_paddle(paddle, xcor, ycor):
    """This function will be create a paddle to use on game"""
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid, stretch_len)
    paddle.penup()
    paddle.goto(xcor, ycor)


def move_up(paddle):
    """Move a paddle to up, setting y position of paddle"""
    y = paddle.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle.sety(y)


def move_down(paddle):
    """Move a paddle to down, setting y position of paddle"""
    y = paddle.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle.sety(y)


def paddle_1_up():
    """Call move up to paddle 1"""
    move_up(paddle_1)


def paddle_2_up():
    """Call move up to paddle 2"""
    move_up(paddle_2)


def paddle_1_down():
    """Call move down to paddle 1"""
    move_down(paddle_1)


def paddle_2_down():
    """Call move down to paddle 2"""
    move_down(paddle_2)


def set_ball():
    """Create ball will be create a rectangle ball to use on game"""
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1
    ball.dy = 1


def main():
    score_1 = 0
    score_2 = 0
    set_screen()
    listen_keyboard()
    game_hud()
    set_paddle(paddle_1, -350, 0)
    set_paddle(paddle_2, 350, 0)
    set_ball()

    while True:
        screen.update()

        # ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # collision with the upper wall
        if ball.ycor() > 290:
            os.system(PLAY_BOUNCE_SOUND)
            ball.sety(290)
            ball.dy *= -1

        # collision with lower wall
        if ball.ycor() < -290:
            os.system(PLAY_BOUNCE_SOUND)
            ball.sety(-290)
            ball.dy *= -1

        # collision with left wall
        if ball.xcor() < -390:
            score_2 += 1
            hud.clear()
            hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
            os.system(PLAY_BLEEP_SOUND)
            ball.goto(0, 0)
            ball.dx *= -1

        # collision with right wall
        if ball.xcor() > 390:
            score_1 += 1
            hud.clear()
            hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
            os.system(PLAY_BLEEP_SOUND)
            ball.goto(0, 0)
            ball.dx *= -1

        # collision with the paddle 1
        if ball.xcor() == paddle_1.xcor()+20 and \
                paddle_1.ycor()+50 > ball.ycor() > paddle_1.ycor()-50 and \
                not ball.xcor() < paddle_1.xcor():
            ball.dx *= -1
            os.system(PLAY_BOUNCE_SOUND)

        # collision with the paddle 2
        if ball.xcor() == paddle_2.xcor()-20 and \
                paddle_2.ycor()+50 > ball.ycor() > paddle_2.ycor()-50 and \
                not ball.xcor() > paddle_2.xcor():
            ball.dx *= -1
            os.system(PLAY_BOUNCE_SOUND)


if __name__ == '__main__':
    main()



