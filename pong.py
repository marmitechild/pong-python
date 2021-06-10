



import turtle

wn = turtle.Screen()
wn.title("if you are reading this you must like marmite or else")    
wn.bgcolor("purple")
wn.setup(width=800,height=600)
wn.tracer(0)

#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=0.5

# function
def paddle_a_up():
    y=paddle_a.ycor()
    y=y+20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y=y-20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y=y+20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y=y-20
    paddle_b.sety(y)


# function FOR BALL
def ball_up():
    y=ball.ycor()
    y=y+20
    ball.sety(y)

def ball_down():
    y=ball.ycor()
    y=y-20
    ball.sety(y)

def ball_right():
    x=ball.xcor()
    x=x+20
    ball.setx(x)

def ball_left():
    x=ball.xcor()
    x=x-20
    ball.setx(x)
# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# BALL MOVEMENT
wn.onkeypress(ball_down, "y")
wn.onkeypress(ball_up, "g")
wn.onkeypress(ball_right, "h")
wn.onkeypress(ball_left, "j")


while True: 
    wn.update()
    # ball.setx(ball.xcor() + ball.dx)
    # ball.sety(ball.ycor() + ball.dy) 














