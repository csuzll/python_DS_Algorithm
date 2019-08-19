# 最小生成树算法
# 使用的是贪婪的策略

from PriorityQueue import PriorityQueue
from Graph import Graph
from Vertex import Vertex
import sys 

# 最小生成树
def prim(G, start):
    pq = PriorityQueue(1000)  # 优先级队列实例，小数优先
    # 所有顶点初始化
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPredecessor(None)

    start.setDistance(0) # 起始结点权重设置为0
    pq.buildHeap([(v.getDistance(), v) for v in G]) # 构建最小堆
    while not pq.isEmpty():
        currentVert = pq.dequeue()
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getWeight(nextVert)
            if nextVert in pq and newCost < nextVert.getDistance():
                nextVert.setPredecessor(currentVert) # 下一个结点的前导结点为当前结点
                nextVert.setDistance(newCost) # 下一个结点的距离设置为newCost
                pq.decreaseKey(nextVert, newCost) # 重新调整为最小堆

if __name__ == '__main__':
    g = Graph()

    letters = ["A", "B", "C", "D", "E", "F", "G"]

    for c in letters:
        g.addVertex(c)

    g.addEdge("A", "B", 2)
    g.addEdge("A", "C", 3)

    g.addEdge("B", "A", 2)
    g.addEdge("B", "C", 1)
    g.addEdge("B", "D", 1)
    g.addEdge("B", "E", 4)

    g.addEdge("C", "A", 3)
    g.addEdge("C", "B", 1)
    g.addEdge("C", "F", 5)

    g.addEdge("D", "B", 1)
    g.addEdge("D", "E", 1)

    g.addEdge("E", "B", 4)
    g.addEdge("E", "D", 1)
    g.addEdge("E", "F", 1)

    g.addEdge("F", "C", 5)
    g.addEdge("F", "G", 1)

    g.addEdge("G", "F", 1)

    prim(g, g.getVertex("A"))
    for vert in g:
        print(vert.getId(), vert.getDistance())
        path = [] # 最短路径
        while vert != None:
            path.append(vert.getId())
            vert = vert.getPredecessor()
        print(path)