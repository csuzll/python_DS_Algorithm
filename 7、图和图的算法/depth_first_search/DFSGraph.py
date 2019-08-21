# 通用的DFS算法
from Graph import Graph
from Vertex import Vertex

class DFSGraph(Graph):
    def __init__(self):
        super(DFSGraph, self).__init__()
        self.time = 0 # 实例变量时间

    def dfs(self):
        # 图中的所有顶点的颜色设置为白色，前导结点设置为（-1）
        for aVertex in self:
            aVertex.setColor("white")
            aVertex.setPredecessor(-1)
        # 对图中的所有白色顶点进行迭代深度遍历
        """迭代所有顶点而不是简单地从所选择的起始顶点进行搜索是为了确保图中的所有顶点都被考虑到，没有顶点从深度优先森林中被遗漏。"""
        for aVertex in self:
            if aVertex.getColor() == "white":
                self.dfsvisit(aVertex)

    # 从某个起始顶点开始搜索
    def dfsvisit(self, startVertex):
        startVertex.setColor("gray") # 起始顶点设置为灰色，代表被访问
        self.time += 1
        startVertex.setDiscovery(self.time) # 设置起始顶点访问之前的步骤数
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == "white":
                nextVertex.setPredecessor(startVertex) # 设置起始顶点的邻接顶点的前导结点为起始结点
                self.dfsvisit(nextVertex) # 递归探索邻接结点
        startVertex.setColor("black") # 起始结点的邻接结点访问完后，设置为黑色
        self.time += 1
        startVertex.setFinish(self.time) # 设置起始结点变为黑色之前的步骤数

    # 拓扑排序(进行深度搜索时每个结点的完成时间从大到小排序就是拓扑排序)
    def toposort(self):
        self.dfs()
        result = []
        # 目前存放了图的所有顶点
        for aVertex in self: 
            result.append(aVertex)
        # 按访问完成时间从大到小排序
        result.sort(key = lambda x: x.finish, reverse=True)
        return result

    # 图的转置(转置之前把图g所有属性回到默认状态)
    def transpose(self):
        gt = DFSGraph()
        for aVertex in self:
            aVertex.setColor("white")
            aVertex.setPredecessor(None)
            aVertex.setDiscovery(0) 
            aVertex.setFinish(0)
            for w in aVertex.getConnections():
                gt.addEdge(w.getId(), aVertex.getId())
        return gt

if __name__ == '__main__':
    g = DFSGraph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)
    g.dfs()
    for vertex in g:
        print(vertex.getId(), vertex.discovery)

    gt = g.transpose()
    for i in range(6):
        print(gt.getVertex(i))


    G = DFSGraph()
    G.addEdge("3/4_cup_milk", "1_cup_mix")
    G.addEdge("1_egg", "1_cup_mix")
    G.addEdge("1_Tbl_Oil", "1_cup_mix")
    G.addEdge("1_cup_mix", "pour_1/4_cup")
    G.addEdge("1_cup_mix", "heat_syrup")
    G.addEdge("heat_syrup", "eat")
    G.addEdge("heat_griddle", "pour_1/4_cup")
    G.addEdge("pour_1/4_cup", "turn_when_bubbly")
    G.addEdge("turn_when_bubbly", "eat")
    G.dfs()
    for vertex in G:
        print(vertex.getId(), vertex.discovery)

    res = G.toposort()
    for v in res:
        print(v.getId(), end=" ")