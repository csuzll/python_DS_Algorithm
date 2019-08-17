# 邻接表实现图类

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
    def getVertices(self, name):
        if name in self.vertList:
            return self.vertList[name]
        else:
            return None

    # 获取图中所有顶点的名称
    def getVertex(self):
        return self.vertList.keys()

    # 通过顶点名称遍历图
    def __contains__(self, name):
        return name in self.vertList

    # 通过顶点对象遍历图
    def __iter__(self):
        return iter(self.vertList.values())

def main():
    g = Graph()

    for i in range(6):
        g.addVertex(i)

    print(g.vertList)

    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    for v in g:
        for w in v.getConnections():
            print("%s, %s" % (v.getId(), w.getId()) )

    n = 0
    if n in g:
        print("YES")

    for v in g:
        print(v)

if __name__ == '__main__':
    main()