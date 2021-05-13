import turtle
import os


""" Code variables
        """
screen = turtle.Screen()
hud = turtle.Turtle()
paddle_1 = turtle.Turtle()
paddle_2 = turtle.Turtle()


def game_hud():
    """ Shows the game's display
        """
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(0, 260)
    hud.write("0:0", align="center", font=("Press Start 2P", 24, "normal"))
    return hud


def window():
    screen.title("My Pong")
    screen.bgcolor("black")
    screen.setup(800, 600)
    screen.tracer(0)


def controls():
    screen.listen()
    screen.onkeypress(paddle_1_up, "w")
    screen.onkeypress(paddle_1_down, "s")
    screen.onkeypress(paddle_2_up, "Up")
    screen.onkeypress(paddle_2_down, "Down")


def set_paddle(paddle, xcor, ycor):
    """ Creates the paddles of the game
        """
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(xcor, ycor)


def move_up(paddle):
    y = paddle.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle.sety(y)


def paddle_1_up():
    move_up(paddle_1)


def paddle_2_up():
    move_up(paddle_2)


def move_down(paddle):
    y = paddle.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle.sety(y)


def paddle_1_down():
    move_down(paddle_1)


def paddle_2_down():
    move_down(paddle_2)


def game_ball():
    """ Create the game's ball
                """
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1
    ball.dy = 1
    return ball


def main():
    score_1 = 0
    score_2 = 0
    window()
    controls()
    game_hud()
    set_paddle(paddle_1, -350, 0)
    set_paddle(paddle_2, 350, 0)
    ball = game_ball()
    while True:
        screen.update()

        # ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

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
            score_2 += 1
            hud.clear()
            hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
            os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
            ball.goto(0, 0)
            ball.dx *= -1

        # collision with right wall
        if ball.xcor() > 390:
            score_1 += 1
            hud.clear()
            hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
            os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
            ball.goto(0, 0)
            ball.dx *= -1

        # collision with the paddle 1
        if ball.xcor() < -330 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
            ball.dx *= -1
            os.system("afplay bounce.wav&")

        # collision with the paddle 2
        if ball.xcor() > 330 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
            ball.dx *= -1
            os.system("afplay bounce.wav&")


if __name__ == '__main__':
    main()
