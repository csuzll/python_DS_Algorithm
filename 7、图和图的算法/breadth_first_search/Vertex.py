# 添加了实例属性的顶点类

class Vertex:
    def __init__(self, name):
        self.id = name # 顶点的名称
        self.connectedTo = {} # 字典表示当前顶点连接到的其他顶点和它们的边的权重，{nbr: weight}
        self.color = "white" # 顶点的颜色
        self.distance = None # 图中此顶点到起始顶点的最小距离 
        self.predecessor = None # 图中此顶点到起始顶点的最小距离路径上此顶点的前一个顶点

    # 从这个顶点添加一个连接(一条边)到另一个顶点
    def addNeighbor(self, nbr, weight=0):
        """nbr为Vertex对象，代表另一个结点对象"""
        self.connectedTo[nbr] = weight

    # 获得顶点颜色
    def getColor(self):
        return self.color

    # 设置顶点颜色
    def setColor(self, color):
        self.color = color

    # 获得到起始顶点的最小距离
    def getDistance(self):
        return self.distance

    # 设置到起始顶点的最小距离
    def setDistance(self, distance):
        self.distance = distance

    # 获得最小距离路径上此顶点的前一个顶点
    def getPredecessor(self):
        return self.predecessor

    # 设置最小距离路径上此顶点的前一个顶点
    def setPredecessor(self, predecessor):
        self.predecessor = predecessor

    # 实现能够直接调用print(Vertex)，输出这个顶点的名称及与此顶点有关的顶点的名称
    def __str__(self):
        return str(self.id) + " connectedTo: " + str([x.id for x in self.connectedTo])

    # 获取此结点的邻接表中的所有顶点对象
    def getConnections(self):
        return self.connectedTo.keys()

    # 获取结点id
    def getId(self):
        return self.id

    # 返回当前结点到某一个顶点的边的权重
    def getWeight(self, nbr):
        return self.connectedTo[nbr]