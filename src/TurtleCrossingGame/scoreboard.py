from turtle import Turtle

class Scoreboard(Turtle):
    ALIGNMENT = "left"
    FONT = ("Courier", 15, "normal")
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
    
    def write_level(self):
        score_string = f"Level: {self.level}"
        self.goto(-270, 270)
        self.write(arg=score_string, move=False, align=self.ALIGNMENT, font=self.FONT)
    
    def increment_level(self):
        self.level += 1
        self.clear()
        self.write_level()
    
    def game_over(self):
        self.goto(-50, 270)
        self.write(arg="GAME OVER.", move=False, align=self.ALIGNMENT, font=self.FONT)
    
    def get_level(self):
        return self.level
    
    def declare_winner(self):
        self.goto(-50, -270)
        self.write(arg="YOU WIN!!!", move=False, align=self.ALIGNMENT, font=self.FONT)
    