import turtle
import os

from random import randint, choice
from time import sleep

from constants import *
from play_sounds import play_sound_bounce, play_sound_bleep

""" Code variables"""
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
    screen.title("Pong with Turtle")
    screen.bgcolor("black")
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.tracer(0)


def controls():
    """ Set the game's controls"""
    screen.listen()
    screen.onkeypress(paddle_1_up, "w")
    screen.onkeypress(paddle_1_down, "s")
    screen.onkeypress(paddle_2_up, "Up")
    screen.onkeypress(paddle_2_down, "Down")


def set_paddle(paddle, xcor, ycor):
    """This function will be create a paddle to use on game"""
    paddle.speed("fastest")
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(PLAYER_HEIGHT / CURSOR_SIZE,  PLAYER_WIDTH / CURSOR_SIZE)
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


def game_ball():
    """ Create the game's ball"""
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)


def write_hud_score(score_1, score_2):
    msg = f"{score_1} : {score_2}"
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
    """This function define limit score"""
    if score == 1000000:
        hud.clear()
        msg_1 = f"{player} WINNER"
        msg_2 = "Click to close game"
        font_1 = ("Press Start 2P", 24, "normal")
        font_2 = ("Press Start 2P", 15, "normal")
        hud.write(msg_1, align="center", font=font_1)
        sleep(3)
        hud.clear()
        hud.write(msg_2, align="center", font=font_2)
        screen.exitonclick()


def reset_ball():
    ball.goto(0, 0)
    ball.setheading(choice([0, 180]) + randint(-60, 60))


def move_ball():
    ball.forward(0.05)


def collision_ball_with_wall(score_1, score_2):
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
        ball.setheading(180 - paddle_1.heading())
        ball.setheading(choice([-45, -30, -15, 0, 15, 30, 45]))
        play_sound_bounce()

    # collision with the paddle 2
    elif ball.xcor() < paddle_2.xcor() and \
            abs(ball.xcor() - paddle_2.xcor()) < 15 and \
            abs(ball.ycor() - paddle_2.ycor()) < (PLAYER_HEIGHT/2):
        ball.setheading(180 - paddle_2.heading())
        ball.setheading(choice([-135, -150, -165, 180, 165, 150, 135]))
        play_sound_bounce()


def main():
    score_1 = 0
    score_2 = 0
    set_screen()
    controls()
    game_hud()
    set_paddle(paddle_1, -350, 0)
    set_paddle(paddle_2, 350, 0)
    game_ball()
    while True:
        screen.update()

        # ball movement
        move_ball()

        # collision wall
        score_1, score_2 = collision_ball_with_wall(score_1, score_2)

        set_collision_paddle()


if __name__ == '__main__':
    main()
