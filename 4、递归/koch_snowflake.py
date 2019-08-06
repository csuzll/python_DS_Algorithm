# turtle递归画出Koch snowflake
import turtle

def koch(length, order, myTurtle):
    if order > 0:
        for turn in [0, 60, -120, 60]:
            myTurtle.left(turn)
            koch(length/3., order-1, myTurtle)            
    else:
        myTurtle.forward(length)


def draw_koch(length, order, myTurtle):
    for i in range(3):
        koch(length, order, myTurtle)
        myTurtle.right(120)
        
myTurtle = turtle.Turtle()
myWin = turtle.Screen()
myTurtle.pensize(2)
myTurtle.speed(10)
myTurtle.goto(0, 0)
myTurtle.down()
draw_koch(100., 3, myTurtle)