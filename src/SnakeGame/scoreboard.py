from turtle import Turtle

class ScoreBoard(Turtle):
    ALIGNMENT = "center"
    FONT = ('Courier New', 15, 'normal')

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/workspaces/100Days/src/SnakeGame/highscore.txt", "r") as file:
            self.highscore = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_score()
        
    def write_score(self):
        score_string = f"Score: {self.score} Highscore: {self.highscore}"
        self.goto(0, 280)
        self.write(arg=score_string, move=False, align=self.ALIGNMENT, font=self.FONT)
    
    def increment_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore += 1
        self.clear()
        self.write_score()
    
    def game_over(self):
        # write highscore to the file
        with open("/workspaces/100Days/src/SnakeGame/highscore.txt", "w") as file:
            file.write(str(self.highscore))
        self.home()
        self.write(arg="GAME OVER.", move=False, align=self.ALIGNMENT, font=self.FONT)
    