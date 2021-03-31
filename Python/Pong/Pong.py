import turtle
import functools

wn = turtle.Screen()
wn.title("pong tutorial by tokyoedtech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)
#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)
#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()

#Function
def movePaddle(paddle, direction):
    y = paddle.ycor()
    y += 20
    paddle.sety(y)

#keyboard input
wn.listen()
wn.onkeypress(functools.partial(movePaddle, paddleA, "up"),"w")
wn.onkeypress(functools.partial(movePaddle, paddleA, "down"), "s")
wn.onkeypress(functools.partial(movePaddle, paddleB, "up"), "u")
wn.onkeypress(functools.partial(movePaddle, paddleB, "down"), "j")
#game loop
while True:
    wn.update()