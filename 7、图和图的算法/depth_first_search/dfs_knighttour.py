from Graph import Graph
from Vertex import Vertex

"""
骑士之旅是深度优先搜索的特殊情况，其目的是创建最深的第一棵树，没有任何分支。
"""

# 1、创建骑士之旅图
def knightGraph(bdSize):
    g = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeID = posToNodeId(row, col, bdSize) # 对棋盘每个方格做顶点编号
            nextMoves = genLegalMoves(row, col, bdSize) # 获取骑士下一步能到达的顶点
            # 转换为图中的边
            for pos in nextMoves:
                g.addEdge(nodeID, pos)
    return g

# 根据行和列将棋盘上的位置转换为对应的顶点的顶点ID
def posToNodeId(row, column, board_size):
    return (row * board_size) + column

# 创建某个位置的可移动列表(边)
def genLegalMoves(row, col, size):
    nextMoves = [] # 可移动列表
    moveOffset = [(-1,2), (1,2), (-2,1), (2,1), (-2,-1), (2,-1), (-1, -2), (1,-2)] # 8个可移动偏移量
    for i in moveOffset:
        x = row + i[0]
        y = col + i[1]
        if legalCoord(x, size) and legalCoord(y, size): # 判断该坐标是否在棋盘上
            nodeId = posToNodeId(x, y, size)
            nextMoves.append(nodeId)
    return nextMoves

# 判断生成的行标或者列标是否存在棋盘上
def legalCoord(x, size):
    if x >=0 and x < size:
        return True
    else:
        return False

# 2、骑士旅行的深度优先搜索（明确禁止一个顶点被多次访问）
"""
下述代码中的深度遍历中，复杂发为O(k^N)，K为常数，N为顶点个数，随着顶点数增加，
算法复杂度指数级增长，对于5*5的方格能较快完成，而对于8*8的方格，得几小时才能完成算法。

"""
def knightTour(n, path, u, limit):
    """
    n: 遍历顶点数，初始为0
    path: 到此为止访问的顶点列表
    u: 当前顶点
    limit: 限制访问的顶点数
    """
    u.setColor("gray") # 设置为灰色，表示正在访问
    path.append(u) # 将当前顶点加入顶点访问列表
    if n < limit: # 顶点未访问完
        nbrList = list(u.getConnections()) # 当前顶点的邻接顶点列表
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == "white": # 邻接顶点未被访问过
                done = knightTour(n+1, path, nbrList[i], limit)
            i = i + 1
        # 如果已经到达无相邻结点的结点且到此为止访问的顶点数还未有64个，则回溯
        # 即弹出上一个访问的结点并设置其为白色，回到未访问状态
        if not done:
            path.pop()
            u.setColor("white")
    else:
        # 所有结点已经被访问
        done = True
    return done

# 骑士旅行的深度优先搜索算法改进
"""
棋盘边缘的顶点边数较少，棋盘中央的顶点边数多，若先访问棋盘边缘的顶点，再访问棋盘中央的顶点，能降低算法复杂度。
"""
def knightTour2(n, path, u, limit):
    u.setColor("gray")
    path.append(u)
    if n < limit:
        nextVerts = orderByAvail(u) # 排序后的邻接结点
        i = 0
        done = False
        while i < len(nextVerts) and not done:
            if nextVerts[i].getColor() == "white":
                done = knightTour(n+1, path, nextVerts[i], limit)
            i = i + 1
        if not done:
            path.pop()
            u.setColor("white")
    else:
        done = True
    return done

# 将结点n的邻接结点按邻接结点的可移动顶点数从小到大排序
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == "white":
            c = 0
            for w in v.getConnections():
                if w.getColor() == "white":
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x : x[0])
    return [y[1] for y in resList]


if __name__ == '__main__':
    g = knightGraph(8)
    start = g.getVertex(1)
    print(start)
