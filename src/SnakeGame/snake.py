from re import T
from turtle import Turtle

class Snake:
    RIGHT = 0
    LEFT = 180
    UP = 90
    DOWN = 270
    MOVE_DISTANCE = 20

    def __init__(self):
        self.segments = []
        self.build_snake()
        
    def build_snake_segment(self, pos):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos)
        segment.speed(2)
        self.segments.append(segment)
    
    def build_snake(self):
        start_pos = [(0, 0), (-20, 0), (-40, 0)]

        for pos in start_pos:
            self.build_snake_segment(pos)
        
    def get_snake(self):
        return self.segments
    
    def get_snake_head(self):
        return self.get_snake()[0]
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            prev_seg_x = self.segments[seg_num - 1].xcor()
            prev_seg_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(prev_seg_x, prev_seg_y)
        
        self.get_snake_head().forward(self.MOVE_DISTANCE)
    
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
        
    def grow_snake(self):
        last_seg_pos = self.segments[-1].position()
        self.build_snake_segment(last_seg_pos)
    
    def is_colliding_with_wall(self):
        if self.get_snake_head().xcor() > 290 or \
            self.get_snake_head().xcor() < -290 or \
            self.get_snake_head().ycor() > 290 or \
            self.get_snake_head().ycor() < -290:
            return True
        
        return False
    
    def is_colliding_with_body(self):
        for segment in self.segments[1:]:
            if self.get_snake_head().distance(segment) < 10:
                return True
        
        return False