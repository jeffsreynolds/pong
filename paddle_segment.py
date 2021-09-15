from tkinter.constants import S, Y
from turtle import Turtle

class PaddleSegment(Turtle):
    def __init__(self, paddle_colour, x_position, y_offset, x_strength) -> None:
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color(paddle_colour)
        self.x_position = x_position
        self.y_offset = y_offset

        self.x_strength = x_strength
        self.y_strength = 0

        self.x_speed = 0
        self.reposition()

    def reposition(self):
        self.goto(self.x_position, self.y_offset)

    def move(self, speed):
        self.goto(self.xcor(), self.ycor() + speed)

    def check_collision(self, ball):
        if self.distance(ball) < ball.size * 20 and \
            ( # make sure that the ball is moving towards paddle segment
                (self.xcor() > 0 and ball.x_speed > 0)
                or
                (self.xcor() < 0 and ball.x_speed < 0)
            ):
            print(f"ball speed was x: {ball.x_speed} y:{ball.y_speed}, adding x:{self.x_strength} y:{self.y_strength}")
            ball.bounce(True, self.x_strength, self.y_strength)

    def update_speed(self, speed):
        self.y_strength = speed