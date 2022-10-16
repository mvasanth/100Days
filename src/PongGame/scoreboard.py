from turtle import Turtle

class ScoreBoard(Turtle):
    ALIGNMENT = "center"
    FONT = ('Courier New', 50, 'normal')
    
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.pos = pos
    
    def increment_score(self):
        self.score += 1
    
    def write_score(self):
        home = (0, 0)
        if self.pos == home:
            self.home()
            self.write(arg="GAME OVER.", move=False, align=self.ALIGNMENT, font=self.FONT)
        else:
            score_string = f"{self.score}"
            self.goto(self.pos)
            self.clear()
            self.write(arg=score_string, move=False, align=self.ALIGNMENT, font=self.FONT)
    
    def get_score(self):
        return self.score    
    