from turtle import Turtle

class ScoreBoard(Turtle):
    ALIGNMENT = "center"
    FONT = ('Courier New', 15, 'normal')

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_score()
        
    def write_score(self):
        score_string = f"Score: {self.score}"
        self.goto(0, 280)
        self.write(arg=score_string, move=False, align=self.ALIGNMENT, font=self.FONT)
    
    def increment_score(self):
        self.score += 1
        self.clear()
        self.write_score()
    
    def game_over(self):
        self.home()
        self.write(arg="GAME OVER.", move=False, align=self.ALIGNMENT, font=self.FONT)
    