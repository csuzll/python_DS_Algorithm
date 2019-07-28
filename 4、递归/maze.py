# 迷宫问题

# 给定起点和迷宫信息，找到一条出去的路径

import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+' # +号表示墙壁
DEAD_END = '-' # 

# Maze类来表示迷宫。为了使这个更有趣，将使用turtle模块来绘制和探索迷宫。
class Maze:
    # mazeFileName:迷宫数据文件
    # __init__()读取迷宫的数据文件，初始化迷宫的内部表示，并找到乌龟的起始位置
    def __init__(self, mazeFileName):
        self.mazelist = [] # 迷宫的内部表示：列表的列表mazelist = [[rowList],[rowList],[rowList],[rowList],...]
        rowsInMaze = 0 # 行数
        columnsInMaze = 0 # 列数
        mazeFile = open(mazeFileName,'r')
        for line in mazeFile: # 迷宫文件的一行
            rowList = []
            col = 0
            for ch in line[:-1]: # line[-1]应该是空格吧
                rowList.append(ch)
                if ch == 'S': # S代表乌龟的起始坐标（startRow, startCol）
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze # 行数
        self.columnsInMaze = columnsInMaze # 列数
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2

        self.t = turtle.Turtle() # turtle对象
        self.t.shape('turtle')
        self.wn = turtle.Screen() # 绘制窗口对象，默认坐标原点在canvas中心(不符合要求)
        # 自定义坐标: setworldcoordinates(llx,lly,urx,ury)表示屏幕的左下角的(x,y)和右上角的(x,y)
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5, -(rowsInMaze-1)/2-.5, (columnsInMaze-1)/2+.5, (rowsInMaze-1)/2+.5) 

    # 在屏幕上的一个窗口绘制迷宫
    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    # 如果是墙壁，绘制到屏幕对应位置上，因为原点变了，设置为orange颜色
                    # 矩阵列表中的[y][x]对应屏幕中的[x+xTranslate][yTranslate-y]
                    self.drawCenteredBox(x + self.xTranslate, -y + self.yTranslate, 'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    # drawCenteredBox绘制方格
    def drawCenteredBox(self, x, y, color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90) # 90代表北方向
        self.t.down()
        self.t.begin_fill()
        for i in range(4): # 代表4个方向
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    # 乌龟移动
    def moveTurtle(self, x, y):
        self.t.up()
        # self.t.towards(x,y)返回的是乌龟朝向这个点(x,y)的角度。计算角度时，水平向右为0度，逆时针方向为角度增大的方向。
        self.t.setheading(self.t.towards(x + self.xTranslate, -y + self.yTranslate))
        # 移动到这个点
        self.t.goto(x + self.xTranslate, -y + self.yTranslate)

    # 绘制一个半径为10且颜色为color的原点
    def dropBreadcrumb(self,color):
        self.t.dot(10, color)

    # 更新迷宫的内部表示，并更改乌龟的位置
    def updatePosition(self, row, col, val=None):
        # 用颜色更新线路 
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col,row)

        if val == PART_OF_PATH: # 
            color = 'green' # 绿色代表找到的出迷宫线路
        elif val == OBSTACLE:  # 障碍物
            color = 'red'  
        elif val == TRIED:  # 特定格子
            color = 'black' 
        elif val == DEAD_END: # 格子是死角
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    # 检查当前位置是否是迷宫的退出位置
    # 当乌龟已经到迷宫的边缘时，即行零或列零，或者在最右边列或底部行。
    def isExit(self, row, col):
        return (row == 0 or
                row == self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1 )

    # 重载运算符[]，以便我们的算法可以轻松访问任何特定格的状态
    def __getitem__(self,idx): 
        return self.mazelist[idx]

# 递归函数: 搜索函数
def searchFrom(maze, startRow, startColumn):
    """
    maze: 迷宫对象
    startRow: 起始行
    startColumn: 起始列
    """
    # 从这一点开始，试四个方向，直到找到出路。

    # 几种基本情况返回值:
    #  1. 这一格子被墙壁占据，返回False
    maze.updatePosition(startRow, startColumn) # 这只是为了可视化算法，以便于你可以看到乌龟如何探索通过迷宫
    if maze[startRow][startColumn] == OBSTACLE :
        return False
    #  2. 乌龟找到一个已经探索过的格子，不想继续从这个位置探索，否则会陷入循环。
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False
    #  3. 找到一个外边缘，没有被墙壁占据。换句话说。我们发现了迷宫的一个出口
    if maze.isExit(startRow,startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH) # 将迷宫出去的路径标记为绿色
        return True
    # 如果以上都不为真，则继续探索
    maze.updatePosition(startRow, startColumn, TRIED)
    # 使用or轮流尝试每个方向(如果需要)。
    # 按顺序为北，南，西，东进行尝试。如果在任何一个方向上调用成功，则后面的不需要调用。
    # 如果所有四个递归调用返回 False，那么认为是一个死胡同
    found = searchFrom(maze, startRow-1, startColumn) or \
            searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
            searchFrom(maze, startRow, startColumn+1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


myMaze = Maze('maze.txt')
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow,myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)
