import turtle
import os

""" Code variables"""
screen = turtle.Screen()
hud = turtle.Turtle()
paddle_1 = turtle.Turtle()
paddle_2 = turtle.Turtle()


def game_hud():
    """ Shows the game's display"""
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(0, 260)
    hud.write("PLAYER > 0 :  PLAYER 2 >  0",
              align="center", font=("Press Start 2P", 24, "normal"))
    return hud


def window():
    """ Create the game's window"""
    screen.title("My Pong")
    screen.bgcolor("black")
    screen.setup(800, 600)
    screen.tracer(0)


def controls():
    """ Set the game's controls"""
    screen.listen()
    screen.onkeypress(paddle_1_up, "w")
    screen.onkeypress(paddle_1_down, "s")
    screen.onkeypress(paddle_2_up, "Up")
    screen.onkeypress(paddle_2_down, "Down")


def set_paddle(paddle, xcor, ycor):
    """ Creates the paddles of the game"""
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(xcor, ycor)


def move_up(paddle):
    """ Move the paddles upwards"""
    y = paddle.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle.sety(y)


def paddle_1_up():
    """ Move the left paddle up"""
    move_up(paddle_1)


def paddle_2_up():
    """ Move the right paddle up"""
    move_up(paddle_2)


def move_down(paddle):
    """ Move the paddles downwards"""
    y = paddle.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle.sety(y)


def paddle_1_down():
    """ Move the left paddle down"""
    move_down(paddle_1)


def paddle_2_down():
    """ Move the left paddle down"""
    move_down(paddle_2)


def game_ball():
    """ Create the game's ball"""
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1
    ball.dy = 1
    return ball


def update_score(score_1, score_2, player_1, player_2, ball):
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} > {} :  {} >  {}".format(player_1, score_1, player_2, score_2),
                  align="center", font=("Press Start 2P", 24, "normal"))
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1
        return score_1

    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} > {} :  {} >  {}".format(player_1, score_1, player_2, score_2),
                  align="center", font=("Press Start 2P", 24, "normal"))
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1
        return score_2


def limit_score(score, player):
    if score == 10:
        hud.clear()
        hud.write(" THIS PLAYER WINNER > {} ".format(player),
                  align="center", font=("Press Start 2P", 24, "normal"))
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        hud.write(" click from close game",
                  align="left", font=("Press Start 2P", 10, "normal"), move=True)
        screen.exitonclick()


def sum_ball(ball):
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


def set_collision_wall_ball(ball):
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


def set_collision_paddle(ball, paddle_1, paddle_2):
    # collision with the paddle 1
    if ball.xcor() == paddle_1.xcor() + 20 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50 and \
            not ball.xcor() < paddle_1.xcor():
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    # collision with the paddle 2
    if ball.xcor() == paddle_2.xcor() - 20 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50 and \
            not ball.xcor() > paddle_2.xcor():
        ball.dx *= -1
        os.system("afplay bounce.wav&")


def main():
    """ Main function of the game"""
    score_1 = 0
    score_2 = 0
    player_1 = 'PLAYER 1 '
    player_2 = 'PLAYER 2 '
    window()
    controls()
    game_hud()
    set_paddle(paddle_1, -350, 0)
    set_paddle(paddle_2, 350, 0)
    ball_1 = game_ball()
    while True:
        screen.update()

        # ball movement
        sum_ball(ball_1)

        # collision wall
        set_collision_wall_ball(ball_1)

        # collision with left wall
        if ball_1.xcor() < -390:
            score_2 = update_score(score_1, score_2, player_1, player_2, ball_1)
            limit_score(score_2, player_2)

        # collision with right wall
        if ball_1.xcor() > 390:
            score_1 = update_score(score_1, score_2, player_1, player_2, ball_1)
            limit_score(score_1, player_1)

        set_collision_paddle(ball_1, paddle_1, paddle_2)


if __name__ == '__main__':
    main()
