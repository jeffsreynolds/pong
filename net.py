from turtle import Turtle

DOWN = 270

class Net(Turtle):
    def __init__(self, screen_height, colour) -> None:
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.goto(0, screen_height / 2)
        self.setheading(DOWN)
        self.color(colour)
        self.hideturtle()
        
        for _ in range(int(screen_height), int(screen_height / 2 - screen_height), int(-(screen_height / 20))):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
