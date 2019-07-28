import turtle

# 下面是一个turtle使用的简单例子
myTurtle = turtle.Turtle() # 创建一个turtle对象
myWin = turtle.Screen() # 创建一个窗口对象来绘制

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0: # 线的长度大于0
        myTurtle.forward(lineLen) # 以linelen的长度前进
        myTurtle.right(90) # 然后向右转90度
        drawSpiral(myTurtle, lineLen-5) # 再次调用drawSpir​​al并缩短长度递归

drawSpiral(myTurtle, 100)
myWin.exitonclick() # 单击窗口，然后程序清理并退出。