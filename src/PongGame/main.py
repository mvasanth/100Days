from turtle import Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

def main():
    MAX_SCORE = 5
    L_SCOREBOARD_POS = (-100, 200)
    R_SCOREBOARD_POS = (100, 200)

    window = Screen()
    window.title("Welcome to a game of Pong!")
    window.setup(width=800, height=600)
    window.bgcolor("black")
    window.tracer(0)

    l_paddle = Paddle((-350, 0))
    l_scoreboard = ScoreBoard()
    l_scoreboard.write_score(L_SCOREBOARD_POS)

    r_paddle = Paddle((350, 0))
    r_scoreboard = ScoreBoard()
    r_scoreboard.write_score(R_SCOREBOARD_POS)
    
    ball = Ball()

    window.listen()
    window.onkey(l_paddle.move_up, "w")
    window.onkey(l_paddle.move_down, "s")
    window.onkey(r_paddle.move_up, "Up")
    window.onkey(r_paddle.move_down, "Down")

    ball.move()
    window.update()

    is_game_on = True

    while is_game_on:
        window.update()
        time.sleep(ball.get_move_speed())
        ball.move()

        # Detect collision with the wall
        if ball.is_colliding_with_wall():
            ball.bounce_y()
        
        # Detect collision with either of the paddles 
        if ball.distance(r_paddle) < 50 and ball.xcor() >= (r_paddle.xcor() - 20) \
            or ball.distance(l_paddle) < 50 and ball.xcor() <= (l_paddle.xcor() + 20):
                ball.bounce_x()
        
        # Right player has missed the ball
        if ball.xcor() >= 380:
            ball.reset_position()
            l_scoreboard.increment_score()
            l_scoreboard.write_score(L_SCOREBOARD_POS)
        
        # Left player has missed the ball
        if ball.xcor() <= -380:
            ball.reset_position()
            r_scoreboard.increment_score()
            r_scoreboard.write_score(R_SCOREBOARD_POS)
        
        # Game ending logic
        # if r_paddle.get_score() == MAX_SCORE \
        #     or l_paddle.get_score == MAX_SCORE:
        #     is_game_on = False
            
    window.exitonclick()

main()