# ------------------------------------------------------------
# 🕹️ Gaming App using Python Turtle
#
# 📦 Required Libraries:
#     pip install PythonTurtle
#
# 🚀 How to Run:
# 1. Save this code as gamingApp.py
# 2. Run it using: python gamingApp.py
# 3. Use Left/Right arrow keys to move the paddle and catch the ball.
# ------------------------------------------------------------

import turtle, random

t = turtle.Turtle()
t.speed(0)
t.shape("square")
t.color("blue")
t.penup()
t.goto(0, -150)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(random.randint(-150, 150), 150)

score = 0

def move_left():
    x = t.xcor() - 20
    if x > -200:
        t.setx(x)

def move_right():
    x = t.xcor() + 20
    if x < 200:
        t.setx(x)

def move_ball():
    global score
    y = ball.ycor() - 5
    ball.sety(y)

    if ball.ycor() < -150 and abs(ball.xcor() - t.xcor()) < 20:
        score += 1
        print("Score:", score)
        ball.goto(random.randint(-150, 150), 150)

    elif ball.ycor() < -200:
        print("Game Over! Final Score:", score)
        turtle.bye()
        return

    turtle.ontimer(move_ball, 50)

turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")

move_ball()
turtle.mainloop()
