from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self, shape, size, colour) -> None:
        super().__init__(shape)
        self.penup()
        self.shape(shape)
        self.shapesize(size)
        self.color(colour)
        
        self.size = size
        self.next_point()

    def bounce(self, x_bounce, x_strength, y_strength):
        if x_bounce:
            if self.x_speed < 0:
                self.x_speed = -self.x_speed + x_strength
            else:
                self.x_speed = -self.x_speed - x_strength

            if self.y_speed < 0:
                self.y_speed -= y_strength
            else:
                self.y_speed += y_strength

        if self.x_speed > 40: self.x_speed = 40
        if self.x_speed < -40: self.x_speed = -40

        else: 
            if self.y_speed < 0:
                self.y_speed = -self.y_speed + y_strength
            else:
                self.y_speed = -self.y_speed - y_strength
        
        print(f"ball speed is now x: {self.x_speed} y:{self.y_speed}")


    def move(self):
        self.goto(self.position()[0] + self.x_speed, self.position()[1] + self.y_speed)


    def next_point(self):
        self.goto(0,0)
        self.x_speed = random.choice((-4, -3, -2, 2, 3, 4))
        self.y_speed = random.choice((-1, 0, 1))
        
        
