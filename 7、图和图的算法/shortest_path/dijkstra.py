# dijkstra算法: 求某一特定顶点到任意其他顶点的最短路径
# 使用的是一种广度优先策略
# 分别以图中每个顶点为源点调用V次dijkstra算法，能够得到任意两点间的最短路径。还有另外一种方法叫floyd算法可以求任意两点间的最短路径。它的实现在floyd.py中。

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
    while not pq.isEmpty():
        # 每次从队列中挑选权重最小的边
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
    for i in ["u", "v", "w", "x", "y", "z"]:
        g.addVertex(i)

    g.addEdge("u", "v", 2)
    g.addEdge("u", "w", 5)
    g.addEdge("u", "x", 1)

    g.addEdge("v", "u", 2)
    g.addEdge("v", "w", 3)
    g.addEdge("v", "x", 2)

    g.addEdge("w", "u", 5)
    g.addEdge("w", "v", 3)
    g.addEdge("w", "x", 3)
    g.addEdge("w", "y", 1)
    g.addEdge("w", "z", 5)

    g.addEdge("x", "u", 1)
    g.addEdge("x", "v", 2)
    g.addEdge("x", "w", 3)
    g.addEdge("x", "y", 1)

    g.addEdge("y", "w", 1)
    g.addEdge("y", "x", 1)
    g.addEdge("y", "z", 1)

    g.addEdge("z", "w", 5)
    g.addEdge("z", "y", 1)

    # "u"顶点到任意顶点的最短路径
    dijstra(g, g.getVertex("u"))

    for vert in g:
        print(vert.getId(), vert.getDistance())
        path = [] # 最短路径
        while vert != None:
            path.append(vert.getId())
            vert = vert.getPredecessor()
        print(path)