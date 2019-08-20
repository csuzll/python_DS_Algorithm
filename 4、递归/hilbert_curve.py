# 使用turtle画出hilbert曲线

# 将问题分解成画“三笔凸包”和连接线

import turtle

def draw_hilbert(myTurtle, x0, y0, xis, yis, xjs, yjs, n):
    """
    x0 和 y0是左下角的坐标；
    xis 和 yis是右下角坐标（凸包的终点方向）；
    xjs 和 yjs是左上角坐标（下一笔方向）；
    上述坐标皆是相对于缺口朝下的方向。
    """
    if n <= 0:
        myTurtle.goto(x0+(xis+yis)/2, y0+(xjs+yjs)/2);
    else:
        draw_hilbert(myTurtle, x0, y0, yis/2, xis/2, yjs/2, xjs/2, n-1)  # 画左下角分区 
        draw_hilbert(myTurtle, x0+xis/2, y0+xjs/2 ,xis/2, yis/2, xjs/2, yjs/2, n-1)  # 画左上角分区 
        draw_hilbert(myTurtle, x0+xis/2+yis/2, y0+xjs/2+yjs/2, xis/2, yis/2, xjs/2, yjs/2,n-1)  # 画右上角分区 
        draw_hilbert(myTurtle, x0+xis/2+yis, y0+xjs/2+yjs, -yis/2, -xis/2, -yjs/2, -xjs/2, n-1)  # 画右下角分区 

if __name__ == '__main__':
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myTurtle.up()
    myTurtle.goto(0, 0)
    myTurtle.down()

    draw_hilbert(myTurtle, 0., 0., 300., 0., 0., 300., 3)
    myWin.exitonclick()