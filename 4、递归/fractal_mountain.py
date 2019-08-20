# 绘制一个分形山
import turtle

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()
    
def drawPlatform(points,color,myTurtle):
    """画一个梯形的平台,其实也可以直接写一个drawPolygon的方法"""
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[3][0],points[3][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def mountain(width,level,color,myTurtle):
    if width > 9:
        drawTriangle([(-width/2.,level),(-width/3.,level+width/3.),(-width/6.,level)],
                     color,myTurtle)
        drawTriangle([(width/6.,level),(width/3.,level+width/3.),(width/2.,level)],
                     color,myTurtle)
        drawPlatform([(-width/3.,level),(-width/6.,level+width/3.),
                      (width/6.,level+width/3.),(width/3.,level)],
                     color,myTurtle)
        mountain(width/3.,level+width/3.,color,myTurtle)
    else:
        drawTriangle([(-width/2.,level),(0.,level+width),(width/2.,level)],
                     color,myTurtle)

def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myTurtle.color("white")
    mountain(900, -450, "blue", myTurtle)
    myWin.exitonclick()

if __name__ == '__main__':
    main()