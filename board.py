import constants as c

from turtle import TurtleScreen
from turtle import Screen
from ball import Ball
from net import Net
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=c.SCREEN_WIDTH, height=c.SCREEN_HEIGHT)
screen.bgcolor(c.SCREEN_COLOUR)
screen.tracer(0)


net = Net(c.SCREEN_HEIGHT, c.NET_COLOUR)
ball = Ball(c.BALL_SHAPE, c.BALL_SIZE, c.BALL_COLOUR)

left_paddle = Paddle("left", c.SCREEN_WIDTH, c.SCREEN_HEIGHT, \
    c.PADDLE_LENGTH, c.PADDLE_COLOUR, c.PADDLE_STRENGTH)

right_paddle = Paddle("right", c.SCREEN_WIDTH, c.SCREEN_HEIGHT, \
    c.PADDLE_LENGTH, c.PADDLE_COLOUR, c.PADDLE_STRENGTH)

left_scoreboard = Scoreboard(c.LEFT_SCOREBOARD_X_POSITION, c.SCOREBOARD_Y_POSITION, c.SCOREBOARD_COLOUR, c.SCOREBOARD_FONT, "center")
right_scoreboard = Scoreboard(c.RIGHT_SCOREBOARD_X_POSITION, c.SCOREBOARD_Y_POSITION, c.SCOREBOARD_COLOUR, c.SCOREBOARD_FONT, "center")

screen.listen()
screen.onkey(key=c.LEFT_PADDLE_UP, fun=left_paddle.up)
screen.onkey(key=c.LEFT_PADDLE_DOWN, fun=left_paddle.down)
screen.onkey(key=c.RIGHT_PADDLE_UP, fun=right_paddle.up)
screen.onkey(key=c.RIGHT_PADDLE_DOWN, fun=right_paddle.down)

#screen boundaries
upper_boundary = c.SCREEN_HEIGHT / 2
lower_boundary = -c.SCREEN_HEIGHT / 2
left_boundary = -c.SCREEN_WIDTH / 2
right_boundary = c.SCREEN_WIDTH / 2

playing = True

while playing:
    ball.move()
    left_paddle.move(upper_boundary, lower_boundary)
    right_paddle.move(upper_boundary, lower_boundary)

    screen.update()
    time.sleep(c.GAME_SPEED)

    if ball.ycor() + ball.size * 20 > upper_boundary or \
       ball.ycor() - ball.size * 20 < lower_boundary:
        ball.bounce(False, 0, 0)

    if ball.xcor() > right_boundary:
        left_scoreboard.increase_score(1)
        ball.next_point()

    elif ball.xcor() < left_boundary:
        right_scoreboard.increase_score(1)
        ball.next_point()

    left_paddle.check_collision(ball)
    right_paddle.check_collision(ball)



    


screen.update()



screen.exitonclick()