from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def is_colliding_with_wall(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            return True

        return False
    
    def is_colliding_with_paddle(self, paddle):
        # if self.distance(paddle) < 50 and self.xcor() >= paddle.xcor():
        #     return True
        
        return False
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1