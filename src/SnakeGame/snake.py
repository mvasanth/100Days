from turtle import Turtle

class Snake:
    RIGHT = 0
    LEFT = 180
    UP = 90
    DOWN = 270
    MOVE_DISTANCE = 20

    def __init__(self):
        self.snake = self.build_snake()
        self.snake_len = len(self.snake)
        
    def build_snake(self):
        segments = []
        start_pos = [(0, 0), (-20, 0), (-40, 0)]

        for pos in start_pos:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(pos)
            segments.append(segment)
        
        return segments

    def get_snake(self):
        return self.snake
    
    def get_snake_head(self):
        return self.get_snake()[0]
    
    def get_snake_len(self):
        return self.snake_len
    
    def move(self):
        for seg_num in range(self.snake_len - 1, 0, -1):
            prev_seg_x = self.snake[seg_num - 1].xcor()
            prev_seg_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(prev_seg_x, prev_seg_y)
        
        self.snake[0].forward(self.MOVE_DISTANCE)
    
    def move_up(self):
        if self.get_snake_head().heading() != self.DOWN:
            self.get_snake_head().setheading(self.UP)

    def move_down(self):
        if self.get_snake_head().heading() != self.UP:
            self.get_snake_head().setheading(self.DOWN)

    def move_left(self):
        if self.get_snake_head().heading() != self.RIGHT:
            self.get_snake_head().setheading(self.LEFT)

    def move_right(self):
        if self.get_snake_head().heading() != self.LEFT:
            self.get_snake_head().setheading(self.RIGHT)