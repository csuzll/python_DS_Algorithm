# Sierpinski Triangle（谢尔宾斯基三角形）
import turtle

# 三角形绘制填充的过程
def drawTriangle(points, color, myTurtle):
    # points: 三角形三个点的坐标
    # color: 颜色
    # myTurtle: turtle对象
    myTurtle.fillcolor(color)
    # 指定三角形的某个点，将turtule落在点上
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    # 下面是填充三角形,A->B->C->A形成三角形
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


# 求两点的终点
def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


# 生成sierpinski triangle
def sierpinski(points, degree, myTurtle):
    # points: 为三角形顶点坐标
    # degree: 划分次数
    # myTurtle: turtle对象

    # 颜色表
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]

    # 先绘制最外边的三角形
    drawTriangle(points, colormap[degree], myTurtle)

    # 划分
    if degree > 0:
        # 3个递归调用，每个使在连接中点获得新的三角形
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree - 1, myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree - 1, myTurtle)
        sierpinski([points[2], getMid(points[1], points[2]), getMid(points[0], points[2])], degree - 1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints, 3, myTurtle)
   myWin.exitonclick()

main()