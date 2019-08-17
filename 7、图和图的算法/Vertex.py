# 邻接表的顶点类

class Vertex:
    def __init__(self, name):
        self.id = name # 顶点的名称
        self.connectedTo = {} # 字典表示当前顶点连接到的其他顶点和它们的边的权重，{nbr: weight}

    # 从这个顶点添加一个连接(一条边)到另一个顶点
    def addNeighbor(self, nbr, weight):
        """nbr为Vertex对象，代表另一个结点对象"""
        self.connectedTo[nbr] = weight

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

def main():
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")

    a.addNeighbor(b, 5)
    a.addNeighbor(c, 4)

    print(a)
    print(b)
    print(c)
    print("\n")

    connecVer = a.getConnections()
    for ver in connecVer:
        print(ver)
    print("\n")

    print(a.getId())
    print(b.getId())
    print(c.getId())
    print("\n")

    print(a.getWeight(b))
    print(a.getWeight(c))


if __name__ == '__main__':
    main()