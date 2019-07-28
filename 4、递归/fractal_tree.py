import turtle
import random

# 分形树（对称树）
def fractaltree(branchlen, t):
    if branchlen > 5:
        t.forward(branchlen) # 树干
        t.right(20) # 向右转20度
        fractaltree(branchlen - 15, t) # 右树
        t.left(40) # 向左转40（20+20）
        fractaltree(branchlen - 15, t) # 左树
        t.right(20) # 向右转20，回到树干
        t.backward(branchlen) # 回到起点


# 模拟自然界更真实的树
def fractaltree2(branchlen, t):
    if branchlen > 5:
        angle = random.randrange(15, 45) # 分叉的角度，使得不一定是左右树是对称的

        step = random.randrange(15, 29)
        t.pensize(max(4, branchlen / step * 5)) # 设置画笔的尺寸，越到树顶越小，且左右随机

        if branchlen < 30: # 当到树顶时，颜色变为叶子的绿色
            t.color("green") 

        t.forward(branchlen)
        t.right(angle)
        fractaltree2(branchlen - step, t) # 树枝长度随机
        t.left(angle*2)
        fractaltree2(branchlen - step, t)
        t.right(angle)
        t.backward(branchlen)
        t.color("brown")

def main():
    # # 以下对应第一个函数的测试代码
    # t = turtle.Turtle()
    # myWin = turtle.Screen()

    # t.left(90)
    # t.up()
    # t.backward(100)
    # t.down()
    # t.color("green")
    # fractaltree(75,t)
    # myWin.exitonclick()

    # 以下对应第二个函数的测试代码
    t = turtle.Turtle()
    myWin = turtle.Screen()

    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    fractaltree2(100,t)
    myWin.exitonclick()

if __name__ == '__main__':
    main()