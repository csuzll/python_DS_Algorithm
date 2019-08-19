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
        nvertex = list(self)
        nvertex.sort(key=lambda x : x.finish, reverse=True)
        for aVertex in nvertex:
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

# 将图G转置
def G_transpose(g):
    gt = DFSGraph()
    # 转置
    for aVertex in g:
        for w in aVertex.getConnections():
            gt.addEdge(w.getId(), aVertex.getId())
    return gt

def scc(g):
    g.dfs()
    gt = G_transpose(g)
    gt.dfs()

if __name__ == '__main__':
    g = DFSGraph()

    # 添加顶点
    for i in ["A","B","C","D","E","F","G","H","I"]:
        g.addVertex(i)

    # 添加边
    g.addEdge("A", "B")
    g.addEdge("B", "C")
    g.addEdge("B", "E")
    g.addEdge("C", "F")
    g.addEdge("C", "C")
    g.addEdge("D", "B")
    g.addEdge("D", "G")
    g.addEdge("E", "A")
    g.addEdge("E", "D")
    g.addEdge("F", "H")
    g.addEdge("G", "E")
    g.addEdge("H", "I")
    g.addEdge("I", "F")

    # g.dfs()
    # print(g.getVertex("A").finish)

    # for v in g:
    #     print(v)
    # gt = G_transpose(g)
    # for v in gt:
    #     print(v)

