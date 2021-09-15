from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x_position, y_position, colour, font, alignment) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_position, y_position)
        self.color(colour)
        self.font = font
        self.alignment = alignment
        self.score = 0

        self.update()

    def increase_score(self, amount):
        self.score += amount
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=self.font)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=self.font)
        


