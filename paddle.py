from paddle_segment import PaddleSegment

class Paddle():
    def __init__(\
                self, \
                side, \
                screen_width, \
                screen_height, \
                paddle_length, \
                paddle_colour, \
                paddle_strength) -> None:

        #initialise boundaries
        self.uppper_bound = screen_height / 2
        self.lower_bound = -screen_height / 2

        #initialise paddle x-position and y-offset
        self.side = side
        if side == "left":
            self.x_position = -screen_width / 2 + 20
        else:
            self.x_position = screen_width / 2 - 20
        
        # this is the top left position of the first paddle segment
        self.y_offset = -paddle_length * 10   
        
        #initialise paddle segments
        self.paddle_segments = []
        paddle_strength_increment = paddle_strength * 2 / paddle_length

        for paddle_segment in range(0, paddle_length):
            x_strength = min(paddle_segment, paddle_length - (paddle_segment + 1))

            self.paddle_segments.append(
                PaddleSegment(\
                    paddle_colour, \
                    self.x_position, \
                    self.y_offset + paddle_segment * 20, \
                    x_strength
                )
            )

        self.speed = 0
            
    def up(self):
        print(f"{self.side} paddle moving up")
        if self.speed < 0:
            self.speed = 0
        elif self.speed < 4:
            self.speed += 2

        self.update_paddle_segment_speeds(self.speed)

    def down(self):
        print(f"{self.side} paddle moving down")
        if self.speed > 0:
            self.speed = 0
        elif self.speed > -4:
            self.speed -= 2

        self.update_paddle_segment_speeds(self.speed)

    def move(self, upper_boundary, lower_boundary):
        # check that we're in bounds
        if (self.speed > 0 and self.paddle_segments[-1].ycor() < upper_boundary) or \
            (self.speed < 0 and self.paddle_segments[0].ycor() > lower_boundary):
            for paddle_segment in self.paddle_segments:
                paddle_segment.move(self.speed)


    def check_collision(self, ball):
        for paddle_segment in self.paddle_segments:
            paddle_segment.check_collision(ball)

    def update_paddle_segment_speeds(self, speed):
        for paddle_segment in self.paddle_segments:
            paddle_segment.update_speed(speed)
