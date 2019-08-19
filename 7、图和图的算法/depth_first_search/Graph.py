# 图类
from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertList = {} # 图中的顶点列表字典{顶点名称: 顶点对象}
        self.numVertices = 0 # 图中的顶点数

    # 添加新的顶点到图中
    def addVertex(self, name):
        self.numVertices += 1 
        # 新顶点对象
        newVertex = Vertex(name)
        self.vertList[name] = newVertex
        return newVertex

    # 在图中添加边
    def addEdge(self, fname, tname, weigth=0):
        """
            fname为开始顶点的名称
            tname为结束顶点的名称
            cost为权重
        """
        if fname not in self.vertList: # 如果开始顶点不在图中，则在图中添加开始结点
            nv = self.addVertex(fname)
        if tname not in self.vertList: # 如果结束顶点不在图中，则在图中添加结束顶点
            nv = self.addVertex(tname)
        self.vertList[fname].addNeighbor(self.vertList[tname], weigth)


    # 根据顶点名称返回顶点对象
    def getVertex(self, name):
        if name in self.vertList:
            return self.vertList[name]
        else:
            return None

    # 获取图中所有顶点的名称
    def getVertices(self):
        return self.vertList.keys()

    # 通过顶点名称遍历图
    def __contains__(self, name):
        return name in self.vertList

    # 通过顶点对象遍历图
    def __iter__(self):
        return iter(self.vertList.values())

    # 图的转置
    def G_transpose(self, g):
        gt = Graph()
        # 转置
        for aVertex in g:
            for w in aVertex.getConnections():
                gt.addEdge(w.getId(), aVertex.getId())
        return gt