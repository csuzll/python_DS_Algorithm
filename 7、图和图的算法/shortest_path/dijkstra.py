# 迪杰斯特拉求最短路径
from PriorityQueue import PriorityQueue
from Graph import Graph
from Vertex import Vertex
import sys

# 一个特定顶点到任意顶点之间的最小权重路径
def dijstra(aGraph, start):
    pq = PriorityQueue(1000) # 优先级队列实例，小数优先
    start.setDistance(0) # 设置起始结点到起始结点的权重为0
    # 元组作为优先队列的元素
    pq.buildHeap([(v.getDistance(), v) for v in aGraph]) # 到起始顶点的距离作为优先级队列中的键，图中顶点的键作为优先级队列中的值
    while not pq.isEmpyt():
        currentVert = pq.dequeue() # 队首元素
        for nextVert in currentVert.getConnections():
            # 新的距离 = 当前结点的距离 + 当前结点到下一个结点之间的权重
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance(): # 如果新距离小于当前距离
                nextVert.setDistance(newDist) # 下一个结点设置新的距离
                nextVert.setPredecessor(currentVert) # 下一个结点的前一个结点设置为当前结点
                pq.decreaseKey(nextVert, newDist) # 当队列中的元素的距离改变时，调整优先级队列

if __name__ == '__main__':
    g = Graph()
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
    dijstra(g, g.getVertex(0))
    for vert in g:
        print(vert.getId(), vert.getDistance())
        path = [] # 最短路径
        while vert != None:
            path.append(vert.getId())
            vert = vert.getPredecessor()
        print(path)