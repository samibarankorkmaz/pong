import turtle
import winsound 
import time
import os
import site

game_window = turtle.Screen()
game_window.title("Oyun")
game_window.bgcolor("black")
game_window.setup(width=800, height=600)
game_window.tracer(0) #

paddle_A = turtle.Turtle()
paddle_A.speed(0) #animation, graphical function
paddle_A.shape("square")
paddle_A.color("red")
paddle_A.shapesize(stretch_wid=5, stretch_len=1) #default 20x20 pixels
paddle_A.penup() #kalemi kaldır yani çizgi çizmeden animate et
paddle_A.goto(-350, 0)

paddle_B = turtle.Turtle()
paddle_B.speed(0) #animation, graphical function
paddle_B.shape("square")
paddle_B.color("blue")
paddle_B.shapesize(stretch_wid=5, stretch_len=1) #default 20x20 pixels
paddle_B.penup() #kalemi kaldır yani çizgi çizmeden animate et
paddle_B.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.color("yellow")
ball.shape("square")
ball.penup()
ball.dx = 0.25
ball.dy = -0.25

#Score
score_red = 0
score_blue = 0


#Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player RED: 0   Player BLUE: 0", align="center", font=("Courier", 14, "normal"))

def paddle_a_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_a_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_b_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_b_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)
    

def exit_func():
    os._exit(0)


game_window.listen()
game_window.onkeypress(exit_func, "Escape") 
game_window.onkeypress(paddle_a_up, "w")
game_window.onkeypress(paddle_a_down, "s")
game_window.onkeypress(paddle_b_up, "Up")
game_window.onkeypress(paddle_b_down, "Down")















while True:
    game_window.update()
    if score_red == 3:
        game_window.clearscreen()
        winsound.PlaySound("gameover.wav", winsound.SND_LOOP)
        while True:
            game_window.onkeypress(exit_func, "Escape") 
            pen.color("black")
            pen.goto(0,0)
            game_window.bgcolor("blue")
            pen.write("GAME OVER!", align="center", font=("Arial", 20, "bold"))
            time.sleep(3)
            pen.clear()
            pen.write("WINNER: PLAYER RED!", align="center", font=("Arial", 20, "bold"))
            game_window.bgcolor("red")
            time.sleep(3)
            pen.clear()
            pen.write("PRESS ESC TO EXIT", align="center", font=("Arial", 20, "bold"))
            game_window.bgcolor("green")
            time.sleep(3)
            pen.clear()
            
         
            
            
        
    #to move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #to check border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_red += 1
        pen.clear()
        pen.write("Player RED: {}   Player BLUE: {}".format(score_red, score_blue), align="center", font=("Courier", 14, "normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_blue += 1
        pen.clear()
        pen.write("Player RED: {}   Player BLUE: {}".format(score_red, score_blue), align="center", font=("Courier", 14, "normal"))
    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)




    """ if ball.xcor() + 10 > 340 and ball.ycor() -10 < paddle_B.ycor() + 40 and ball.ycor() +10 > paddle_B.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1 """

    """  if (ball.xcor() < paddle_A.xcor() + 20) & (ball.ycor() -20 <= paddle_A.ycor()) & (ball.ycor() +20 >= paddle_A.ycor() - 100):
        ball.setx(-330)
        ball.dx *= -1 
    if ball.xcor() + 20 > paddle_B.xcor():
        ball.setx(330)
        ball.dx *= -1  """
    
    
    